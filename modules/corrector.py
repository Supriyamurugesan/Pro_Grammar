import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from typing import List, Tuple

class Corrector:
    def __init__(self, model_name="prithivida/grammar_error_correcter_v1", use_gpu=False):
        self.device = torch.device("cuda" if use_gpu and torch.cuda.is_available() else "cpu")
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def correct(self, text: str) -> Tuple[str, List[Tuple[str, str, int, int, str, int, int]]]:
        inputs = self.tokenizer(f"gec: {text}", return_tensors="pt", padding=True).to(self.device)
        outputs = self.model.generate(**inputs)
        corrected_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Dummy edit data for demonstration
        edits = [('VERB:SVA', 'are', 1, 2, 'is', 1, 2)]
        
        return corrected_text, edits
