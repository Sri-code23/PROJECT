import torch
from transformers import BertTokenizer, BertModel
model_name="bert-base-uncased"
tokenizer=BertTokenizer.from_pretrained(model_name)
model=BertModel.from_pretrained(model_name)
input_text="Hey !  i am here to build an AI assistant "
input_ids=tokenizer.encode(input_text,return_tensors="pt")
attention_mask=tokenizer.encode(input_text,return_tensors="pt", max_length=50, padding="max_length", truncation=True)
outputs=model(input_ids,attention_mask=attention_mask)
print(outputs.last_hidden_state.shape)
