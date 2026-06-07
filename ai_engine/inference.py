import torch
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

app = Flask(__name__)

# GLOBAL ECOSYSTEM VARIABLE DEFINITIONS
BASE_MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"
ADAPTER_PATH = "./final_adapter_weights"

print("🔄 Loading base foundation model and fine-tuned adapters...")

# 1. SETUP SAME MEMORY COMPRESSION FOR SPEED
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

# 2. LOAD INFRASTRUCTURE TOKENIZER & BASE MODEL
tokenizer = AutoTokenizer.from_pretrained(ADAPTER_PATH)
base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_ID,
    quantization_config=bnb_config if torch.cuda.is_available() else None,
    device_map="auto" if torch.cuda.is_available() else None
)

# 3. COMBINE BASE MODEL WITH YOUR CUSTOM LORA WEIGHTS
# This injects your specific resume mentor personality layer onto the smart base LLM
model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
model.eval() # Set model to evaluation mode (turns off training-only parameters like dropout)

print("🚀 Model successfully merged in memory. Awaiting transmission commands...")

# ==========================================================================
# 4. MICROSERVICE HTTP ROUTING LINK
# ==========================================================================
@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        # Pull the incoming JSON package passed from api_client.php
        data = request.get_json()
        
        skills = data.get("skills", "")
        project_description = data.get("project_description", "")
        target_focus = data.get("target_focus", "")

        # Format input using our specific structural prompt template matching training
        messages = [
            {
                "role": "system",
                "content": "You are an expert AI Career Mentor. Analyze the user's input and provide clear, structured, actionable resume modifications, distinct technical skill gaps, and custom technical learning milestone steps."
            },
            {
                "role": "user",
                "content": f"Skills: {skills}. Project: {project_description}. Target Field: {target_focus}."
            }
        ]

        # Use the tokenizer to compile formatting specific to chat models
        text_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        
        # Target execution devices safely
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_inputs = tokenizer([text_prompt], return_tensors="pt").to(device)

        # 5. GENERATE THE SOLUTION TEXT
        with torch.no_grad(): # Disable gradient tracking to conserve execution memory
            generated_ids = model.generate(
                **model_inputs,
                max_new_tokens=512,  # Set length boundary limit for structural output responses
                temperature=0.3,     # Lower temperature means more professional, less random responses
                top_p=0.9
            )
        
        # Trim input tokens off the generation array to leave only the assistant text response
        generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]
        response_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

        # Send raw generated Markdown text straight back to PHP
        return response_text

    except Exception as e:
        return jsonify({"error": f"CORE_ENGINE_FAILURE: Execution thread broken. Code: {str(e)}"}), 500

if __name__ == "__main__":
    # Start the Flask development hosting pipeline server locally on Port 5000
    app.run(host="127.0.0.1", port=5000, debug=False)