from transformers import AutoProcessor, PaliGemmaForConditionalGeneration
from PIL import Image
import requests
import torch

# Configuración
model_path = "D:/Descargas Reemplazo/PaligemmaModel"

#url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"
#image = Image.open(requests.get(url, stream=True).raw)

image_path = "D:/Descargas Reemplazo/car.jpg"

image = Image.open(image_path)

#model = PaliGemmaForConditionalGeneration.from_pretrained(model_id).eval()
#processor = AutoProcessor.from_pretrained(model_id)

# Carga el modelo y el tokenizer desde el directorio local
model = PaliGemmaForConditionalGeneration.from_pretrained(model_path).eval()
processor = AutoProcessor.from_pretrained(model_path)

# Instruct the model to create a caption in Spanish
prompt = "caption es"
model_inputs = processor(text=prompt, images=image, return_tensors="pt")
input_len = model_inputs["input_ids"].shape[-1]

with torch.inference_mode():
    generation = model.generate(**model_inputs, max_new_tokens=100, do_sample=False)
    generation = generation[0][input_len:]
    decoded = processor.decode(generation, skip_special_tokens=True)
    print(decoded)
