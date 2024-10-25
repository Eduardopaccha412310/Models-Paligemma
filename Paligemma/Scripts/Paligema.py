from transformers import AutoProcessor, PaliGemmaForConditionalGeneration
from PIL import Image
import torch

def process_image(image_path, text_input):
    image = Image.open(image_path).convert("RGB")
    model_path = "C:/Users/Eduar/Desktop/Eduardo Paccha/Noveno ciclo/Vinculación/Model"
    model = PaliGemmaForConditionalGeneration.from_pretrained(model_path).eval()
    processor = AutoProcessor.from_pretrained(model_path)
    decoded = "init"

    prompt = text_input
    model_inputs = processor(text=prompt, images=image, return_tensors="pt")
    input_len = model_inputs["input_ids"].shape[-1]

    with torch.inference_mode():
        generation = model.generate(**model_inputs, max_new_tokens=100, do_sample=False)
        generation = generation[0][input_len:]
        decoded = processor.decode(generation, skip_special_tokens=True)
        return decoded


