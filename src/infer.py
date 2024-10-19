import transformers
import torch

model_id = "cognitivecomputations/dolphin-2.9.4-llama3.1-8b"

pipeline = transformers.pipeline(
    "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
)

print(pipeline("Hey how are you doing today?")['generated_text'])
