import numpy as np

# df_validation has columns: ['conversation_id', 'is_correct']
# is_correct is 1 if LLM_judge == Human_label, else 0

unique_ids = df_validation['conversation_id'].unique()
n_boot = 5000
boot_accuracies = []

for _ in range(n_boot):
    # 1. Resample CLUSTERS (Conversation IDs), not rows
    resampled_ids = np.random.choice(unique_ids, size=len(unique_ids), replace=True)
    
    # 2. Reconstruct dataframe from resampled clusters
    # (This effectively weights the rows by how often their ID was picked)
    resampled_rows = df_validation[df_validation['conversation_id'].isin(resampled_ids)]
    # Note: A faster way is to join/merge, but this is the logic
    
    # Actually, a vectorized way for speed:
    # Group by ID, get sum of correct and count of items per ID
    grouped = df_validation.groupby('conversation_id')['is_correct'].agg(['sum', 'count'])
    # Resample the groups
    sample_idx = np.random.choice(grouped.index, size=len(grouped), replace=True)
    sample = grouped.loc[sample_idx]
    
    # 3. Compute Weighted Accuracy
    acc = sample['sum'].sum() / sample['count'].sum()
    boot_accuracies.append(acc)

# 4. Inference
boot_accuracies = np.array(boot_accuracies)
ci_lower = np.percentile(boot_accuracies, 2.5)
ci_upper = np.percentile(boot_accuracies, 97.5)
p_value = np.mean(boot_accuracies <= 0.5)

print(f"Pooled Accuracy: {np.mean(boot_accuracies):.3f} [{ci_lower:.3f}, {ci_upper:.3f}]")
print(f"P-value (H0: Acc <= 0.5): {p_value:.4f}")