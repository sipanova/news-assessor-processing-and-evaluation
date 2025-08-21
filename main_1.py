print("Strat executing...")



import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-1B"

pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

result = pipe(
    "What are the best 3 drinks?",
    max_new_tokens = 100,
    do_sample = True,
    top_k = 50,
    top_p = 0.9,
    temperature = 0.7,
    repetition_penalty = 1.1
)

print(result[0]['generated_text'])