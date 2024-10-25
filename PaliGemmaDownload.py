from transformers import AutoTokenizer, PaliGemmaForConditionalGeneration
import os

# Configuración
model_id = "google/paligemma-3b-mix-224"
hf_token = "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"
model_path = "C:/Users/Eduar/Desktop/Eduardo Paccha/Noveno ciclo/Vinculación/Model"

# Crea el directorio si no existe
os.makedirs(model_path, exist_ok=True)

# Carga el modelo y el tokenizer
model = PaliGemmaForConditionalGeneration.from_pretrained(model_id, token=hf_token)
tokenizer = AutoTokenizer.from_pretrained(model_id, token=hf_token)

# Guarda el modelo y el tokenizer en el directorio especificado
model.save_pretrained(model_path)
tokenizer.save_pretrained(model_path)

