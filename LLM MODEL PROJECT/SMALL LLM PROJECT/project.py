#step-1

"""
downloading the required libraries
1.nltk(Natural language tookit )- popular library used for natural language processing.
   In this we are using it for  tokenisation, stemming, lemmatization 
2.spacy - another popular library for natural language processing . 
   we are using it for entity recognization and language modelling
3.tensorfow or Pytorch - we'll use either one as our deep learning framework . 
   Both libraries used for building and training neural networks.
4.hugging face transformers- we are using this library to access pre-trained 
   language models and fine tuning them for our specific purpose.
"""
#to install these libraries, the commands are
#pip install nltk spacy tensorflow transformers torch (around 800 mb of data )

""""""





#step-2
#to download the nltk data 
"""
import nltk     # to download this in jupyter notebook, use this
nltk.download()
"""
#to download this in vscode im using this code 

"""
import nltk
nltk.download('all')   #this helps us to download all the files inside the nltk library (VS code)
"""

"""
import nltk
nltk.download('punkt') 
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('vader_lexicon')
nltk.download('wordnet')
"""





#step-3

import torch
#torch is a popular library for machine learning and deep learning
from transformers import BertTokenizer, BertModel
# BertTokenizer and BertModel are the classes from the transformers library (module)
"""
BertTokenizer - is a class from the ' transformers ' library that helps us to tokenize the input 
text into subwords (smaller units of text) that the Bert model can understand

BertModel-is a class from the ' transformers ' library that represents the pre-trained Bert model
"""






#step- 4
#loading the Pre-Trained Bert model and Tokenizer
model_name="bert-base-uncased"
#here we are using the "bert-base-uncased" for our project since it a popular nlp (natural language processing ) tasks

tokenizer=BertTokenizer.from_pretrained(model_name)
model=BertModel.from_pretrained(model_name)
#here the ' from_pretrained '  is a method or function inside the BertTokenizer and BertTokenizer classes

"""
model_name is the string that is used to specifiy the name of the model we use ( i. e choosen)
model_name is taken inside the method as an attribute or value

BertTokenizer.from_pretrained(model_name)- loads the pre-tarined tokenizer for the specified model


BertModel.from_pretrained(model_name) - loads the pre-tarined Bert model for the specified model
"""

#step - 5 

#setting up a sample input text to test our model
input_text="Hey !  i am here to build an AI assistant "



#step - 6 

#tokenizing the input text 
input_ids=tokenizer.encode(input_text,return_tensors="pt")

"""
here we are using 'encode' method ( function ) of the 'BertTokenizer' to tokenize the input_text.
we are also setting the 'return_tensors="pt"' to return the tokenized input_text as a 'Pytorch' tensor
#########
encode() - the encode method takes the input_text and breaks it down into
subwords (smaller units of text) that the Bert model can understand

return_tensors="pt" - is a argument that tells the encode method to return the tokenized input as a PyTorch Tensor, 
which is a datastructure that can be processed by the bert model.
"""




#step- 7 
#craeting Tensor for the attention mask
attention_mask=tokenizer.encode(input_text,return_tensors="pt", max_length=50, padding="max_length", truncation=True)
# its like giving the filter ot limit to the token generated like maximum length as '50' Tokens





#step - 8 
#running th einput through the Bert Model
outputs=model(input_ids,attention_mask=attention_mask)
"""
here we are passsing the tokenized 'input' and 'attention_mask' to the Bertmodel , 
and storing the output in the 'outputs' variable.
########
we are calling the model object with input_ids and attention_mask tensors as input.
the Bert moedl processes the input and returns a set of output tensors , which are stored in the 'outputs' variable
"""


#step - 9
#printing the output

print(outputs.last_hidden_state.shape)
"""
we are acccessing 'the last_hidden_state' attribute of the 'outputs' object, which contains the final hidden state of the Bertmodel.

we are printing the shape of the 'last_hidden_state' tensor using the 'shape' attribute
"""
