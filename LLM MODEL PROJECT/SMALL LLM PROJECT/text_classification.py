# Use a pipeline as a high-level helper

from transformers import pipeline

classifier = pipeline("text-classification", model="ProsusAI/finbert")
print(classifier("sad"))
print("hvanbui")




