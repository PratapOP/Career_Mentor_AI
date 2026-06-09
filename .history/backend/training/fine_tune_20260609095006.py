import torch

from datasets import load_dataset

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig
)

from peft import (
    LoraConfig
)

from trl import (
    SFTTrainer,
    SFTConfig
)


MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"

DATASET_PATH = "./training/dataset.json"

OUTPUT_DIR = "./backend/models/final_adapter_weights"


def main():

    device = (
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    print(f"Device: {device}")

    dataset = load_dataset(
        "json",
        data_files=DATASET_PATH,
        split="train"
    )

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID
    )

    tokenizer.pad_token = tokenizer.eos_token

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=(
            torch.float16
            if device == "cuda"
            else torch.float32
        )
    )

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        quantization_config=(
            bnb_config
            if device == "cuda"
            else None
        ),
        device_map=(
            "auto"
            if device == "cuda"
            else None
        )
    )

    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj"
        ]
    )

    training_args = SFTConfig(
        output_dir="./trainer_output",
        num_train_epochs=3,
        learning_rate=2e-4,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        logging_steps=1,
        save_strategy="epoch",
        fp16=(device == "cuda"),
        packing=False
    )

    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=peft_config,
        tokenizer=tokenizer,
        args=training_args
    )

    trainer.train()

    trainer.model.save_pretrained(
        OUTPUT_DIR
    )

    tokenizer.save_pretrained(
        OUTPUT_DIR
    )

    print(
        "Training Complete"
    )


if __name__ == "__main__":
    main()