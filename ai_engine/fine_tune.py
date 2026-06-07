import os
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer, SFTConfig

def run_training_pipeline():
    # 1. ENVIRONMENT CONFIGURATION
    model_id = "Qwen/Qwen2.5-1.5B-Instruct"
    dataset_path = "dataset.json"

    print("Checking computing hardware configuration...")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        print("[WARNING]: No CUDA GPU detected. Fine-tuning on a CPU will be extremely slow.")

    # 2. LOAD CUSTOM LOCAL DATASET
    print(f"Loading custom career telemetry data from: {dataset_path}...")
    dataset = load_dataset("json", data_files=dataset_path, split="train")

    # 3. INITIALIZE TOKENIZER MATCHING BASE ARCHITECTURE
    print(f"Initializing tokenizer for: {model_id}...")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token

    # 4. MEMORY OPTIMIZATION LAYER (4-Bit BitsAndBytes Quantization)
    print("Configuring 4-bit model memory quantization parameters...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16 if device == "cuda" else torch.float32
    )

    # 5. LOAD COMPRESSED BASE LLM
    print("Downloading/Loading base foundational model weights...")
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config if device == "cuda" else None,
        device_map="auto" if device == "cuda" else None
    )

    # 6. ATTACH PARAMETER-EFFICIENT LORA ADAPTER DIAGRAM TILES
    print("Configuring Parameter-Efficient Low-Rank Adaptation (LoRA) layers...")
    peft_config = LoraConfig(
        r=16,                         # Rank parameter (size of adapter matrices)
        lora_alpha=32,                # Learning scaling factor 
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"], # Target internal attention parameters
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"         # Language modeling structural setting
    )

    # 7. CONFIGURE TRAINING RUN LOGISTICS
    print("Setting up training execution matrices...")
    training_args = SFTConfig(
        output_dir="./trained_mentor_model",
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4, # Accumulates calculations to simulate larger batch size safely
        learning_rate=2e-4,            # Optimized small adjustment steps for fine-tuning
        logging_steps=1,
        num_train_epochs=3,            # Number of passes through dataset
        fp16=(device == "cuda"),       # Enable fast precision if running on GPU
        optim="paged_adamw_8bit" if device == "cuda" else "adamw_torch",
        packing=False,                 # Do not pack short samples together
    )

    # 8. INITIALIZE SUPERVISED FINE-TUNING TRAINER
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=peft_config,
        tokenizer=tokenizer,
        args=training_args,
    )

    # 9. EXECUTE INFUSION LOOP
    print("🔄 STARTING CORE TRAINING SEQUENCING...")
    trainer.train()

    # 10. PERSIST HARD WORK TO DISK
    print("Saving fine-tuned adapter parameters locally...")
    trainer.model.save_pretrained("./final_adapter_weights")
    tokenizer.save_pretrained("./final_adapter_weights")
    print("🎉 FINE-TUNING EXECUTION SEQUENCE COMPLETED SUCCESSFULLY.")

if __name__ == "__main__":
    run_training_pipeline()