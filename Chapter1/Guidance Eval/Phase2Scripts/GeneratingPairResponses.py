import os
import json
from typing import Dict, Any, Tuple, List

def load_prompts(prompt_file_path: str) -> Dict[str, str]:
    """
    Loads prompts from a JSON file
    Args:
        prompt_file_path (str): Path to the JSON file containing prompts.
    """
    with open(prompt_file_path, "r", encoding="utf-8") as f:
        prompts = json.load(f)

    # Validate loaded prompts
    for key in ["prompt_Determine_Error", "prompt_Determine_Strat_Intent", "prompt_Decision_Making"]:
        if key not in prompts:
            raise ValueError(f"Missing prompt in JSON: {key}")
        if not prompts[key].strip():
            raise ValueError(f"Empty prompt found for key: {key}")
        
    return prompts

def call_model(system_prompt: str, user_prompt: str, model_name: str = "local-llm", local: bool = False) -> str:
    """
    Replace this with your actual model call (e.g., OpenAI, Azure OpenAI, local server).
    Keep it minimal and deterministic for testing.
    """
    # TODO: Implement your API call here.
    if local:
        # Call local model
        pass
    else:
        # Call remote model
        pass

    # Example shape (pseudo):
    # response = client.chat.completions.create(
    #   model=model_name,
    #   messages=[{"role":"system","content":system_prompt},
    #             {"role":"user","content":user_prompt}],
    #   temperature=0.2,
    # )
    # return response.choices[0].message.content
    return f"[MOCK OUTPUT for {model_name}]\n{user_prompt[:200]}..."


def step1_determine_error(H: str, prompt: str, model_name: str) -> str:
    user = f"{prompt}\n\nConversation History (H):\n{H}"
    return call_model(system_prompt=prompt, user_prompt=user, model_name=model_name)


def step2_determine_strategy_intent(H: str, prompt: str, model_name: str) -> Tuple[str, str]:
    user = f"{prompt}\n\nConversation History (H):\n{H}\n\nReturn two fields:\n- z_what: strategy\n- z_why: intention"
    out = call_model(system_prompt=prompt, user_prompt=user, model_name=model_name)
    # Minimal extraction heuristic; adjust if you format the model output as JSON.
    z_what, z_why = "", ""
    for line in out.splitlines():
        if line.lower().startswith("z_what"):
            z_what = line.split(":", 1)[1].strip()
        if line.lower().startswith("z_why"):
            z_why = line.split(":", 1)[1].strip()
    return z_what or out, z_why or out


def step3_decision_making(H: str, e: str, z_what: str, z_why: str, prompt: str, model_name: str) -> str:
    user = (
        f"{prompt}\n\nConversation History (H):\n{H}\n\nInputs from analysis:\n"
        f"- e (student error): {e}\n- z_what (strategy): {z_what}\n- z_why (intention): {z_why}\n\n"
        "Produce a guiding response r that is relevant, useful, and non-direct (no full solution)."
    )
    return call_model(system_prompt=prompt, user_prompt=user, model_name=model_name)


def run_pipeline_on_dataset(
    dataset: List[Dict[str, Any]],
    prompts: Dict[str, str],
    model_name: str
) -> List[Dict[str, Any]]:
    """
    dataset: list of items with keys:
      - conversation_id (str/int)
      - history (str)  # conversation history H
    returns: list of results per item with e, z_what, z_why, r
    """

    # Simple 3-step pipeline per BRIDGE protocol:
    # Step 1: Determine error (e)
    # Step 2: Determine strategy and intention (z_what, z_why)
    # Step 3: Decision-making to produce final response (r)
    results = []
    for item in dataset:
        cid = item.get("conversation_id")
        H = item.get("history", "")
        e = step1_determine_error(H, prompts["prompt_Determine_Error"], model_name)
        z_what, z_why = step2_determine_strategy_intent(H, prompts["prompt_Determine_Strat_Intent"], model_name)
        r = step3_decision_making(H, e, z_what, z_why, prompts["prompt_Decision_Making"], model_name)
        results.append({
            "conversation_id": cid,
            "e": e,
            "z_what": z_what,
            "z_why": z_why,
            "r": r,
        })
    return results

def save_results(output_file: str, results: List[Dict[str, Any]]):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Results saved to {output_file}")


def main():

    # Load prompts
    prompt_file = "../prompt_templates/prompts_tutoring_guidance.json"
    prompts = load_prompts(prompt_file)

    # Load or construct your dataset (D_TUTOR-ORIGINAL)
    # TODO: Replace this mock with real loader. Expect keys: conversation_id, history (H)
    dataset = [
        {"conversation_id": "conv_001", "history": "Student: I divided by 0.\nTutor: What step led you there?\nStudent: ..."},
        {"conversation_id": "conv_002", "history": "Student: I think the derivative of x^2 is 1/x.\nTutor: Let's revisit power rule.\nStudent: ..."},
    ]

    # Choose model pairs
    base_llm = "base-llm-model"
    if_enhanced_llm = "if-enhanced-llm-model"


    # Run pipeline
    base_llm_result = run_pipeline_on_dataset(dataset, prompts, base_llm)
    if_enhanced_llm_result = run_pipeline_on_dataset(dataset, prompts, if_enhanced_llm)

    # Save the results
    save_results("../ResponsePairLog/" + base_llm + "base_results.json", base_llm_result)
    save_results("../ResponsePairLog/" + if_enhanced_llm + "IF_enhanced_results.json", if_enhanced_llm_result)

    # Extract response pairs for evaluation
    # Expected output format per item: {modelID, conversation_id, response_base, response_if_enhanced}
    response_pairs = []
    for base, enhanced in zip(base_llm_result, if_enhanced_llm_result):
        response_pairs.append({
            "modelID": base_llm,
            "conversation_id": base["conversation_id"],
            "response_base": base["r"],
            "response_if_enhanced": enhanced["r"],
        })

    # Save response pairs for later evaluation
    save_results("../Results/response_pairs.json", response_pairs)

if __name__ == "__main__":
    main()