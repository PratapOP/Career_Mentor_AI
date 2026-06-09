import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig
)

from peft import PeftModel


class CareerMentor:

    def __init__(self):

        self.base_model_id = "Qwen/Qwen2.5-1.5B-Instruct"
        self.adapter_path = "./models/final_adapter_weights"

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.tokenizer = None
        self.model = None

        self.load_model()

    def load_model(self):

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=(
                torch.float16
                if self.device == "cuda"
                else torch.float32
            )
        )

        try:

            self.tokenizer = AutoTokenizer.from_pretrained(
                self.adapter_path
            )

            base_model = AutoModelForCausalLM.from_pretrained(
                self.base_model_id,
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
                self.adapter_path
            )

            self.model.eval()

            print(
                "[SUCCESS] Fine-tuned adapter loaded."
            )

        except Exception as e:

            print(
                "[WARNING] Adapter not found."
            )

            print(
                str(e)
            )

            self.tokenizer = AutoTokenizer.from_pretrained(
                self.base_model_id
            )

            self.model = AutoModelForCausalLM.from_pretrained(
                self.base_model_id,
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

            self.model.eval()

            print(
                "[SUCCESS] Base model loaded."
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
                    "Analyze the user's profile. "
                    "Provide resume improvements, "
                    "skill gaps, and a roadmap."
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

        prompt = (
            self.tokenizer
            .apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
        )

        model_inputs = self.tokenizer(
            [prompt],
            return_tensors="pt"
        ).to(self.device)

        with torch.no_grad():

            generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=512,
                temperature=0.3,
                top_p=0.9,
                do_sample=True
            )

        generated_ids = [
            output_ids[len(input_ids):]
            for input_ids, output_ids
            in zip(
                model_inputs.input_ids,
                generated_ids
            )
        ]

        response = self.tokenizer.batch_decode(
            generated_ids,
            skip_special_tokens=True
        )[0]

        return response.strip()