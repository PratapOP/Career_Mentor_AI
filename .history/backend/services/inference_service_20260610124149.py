import torch

from pathlib import Path

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig
)

from peft import PeftModel

from config import (
    MODEL_ID,
    ADAPTER_DIR,
    GENERATION_CONFIG
)


class CareerMentor:

    def __init__(self):

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.tokenizer = None
        self.model = None

        self.load_model()

    def load_model(self):

        adapter_exists = (
            Path(ADAPTER_DIR).exists()
            and
            any(Path(ADAPTER_DIR).iterdir())
        )

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=(
                torch.float16
                if self.device == "cuda"
                else torch.float32
            )
        )

        if adapter_exists:

            print(
                "[INFO] Loading Fine-Tuned Adapter..."
            )

            self.tokenizer = AutoTokenizer.from_pretrained(
                str(ADAPTER_DIR)
            )

            base_model = AutoModelForCausalLM.from_pretrained(
                MODEL_ID,
                quantization_config=(
                    bnb_config
                    if self.device == "cuda"
                    else None
                ),
                device_map=(
                    "auto"
                    if self.device == "cuda"
                    else None
                )
            )

            self.model = PeftModel.from_pretrained(
                base_model,
                str(ADAPTER_DIR)
            )

        else:

            print(
                "[INFO] No Adapter Found. Loading Base Model."
            )

            self.tokenizer = AutoTokenizer.from_pretrained(
                MODEL_ID
            )

            self.model = AutoModelForCausalLM.from_pretrained(
                MODEL_ID,
                quantization_config=(
                    bnb_config
                    if self.device == "cuda"
                    else None
                ),
                device_map=(
                    "auto"
                    if self.device == "cuda"
                    else None
                )
            )

        self.tokenizer.pad_token = (
            self.tokenizer.eos_token
        )

        self.model.eval()

        print(
            "[SUCCESS] Model Loaded"
        )

    def generate(
        self,
        skills,
        project_description,
        target_focus
    ):

        messages = [
            {
                "role": "system",
                "content":
                (
                    "You are an expert AI Career Mentor. "
                    "Provide resume improvements, "
                    "skill gap analysis, "
                    "learning roadmap, "
                    "and project recommendations."
                )
            },
            {
                "role": "user",
                "content":
                (
                    f"Skills: {skills}\n"
                    f"Project: {project_description}\n"
                    f"Target Role: {target_focus}"
                )
            }
        ]

        prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt"
        ).to(self.device)

        with torch.no_grad():

            outputs = self.model.generate(
                **inputs,
                **GENERATION_CONFIG
            )

        generated_text = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return generated_text.strip()