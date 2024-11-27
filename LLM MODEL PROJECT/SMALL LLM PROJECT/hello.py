from transformers import pipeline,Conversation
chatbot=pipeline(model="facebook/blenderbot-400M-distill")
conversation=Conversation("hi ! i am your ai assistanat ")
conversation=chatbot(conversation)