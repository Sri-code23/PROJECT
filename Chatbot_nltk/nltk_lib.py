#Basic Chatbot

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

print("CHATBOT: Welcome !, I am your personal chatbot. Ask me something ..")
quit_statements=["exit", "quit", "bye", "see you", "goodbye", "farewell"]
greeting_statements=["hi", "hello", "hey", "hi there", "hello there",
                      "hey there", "greetings", "good morning", "good afternoon",
                        "good evening"]

user_exited=True
while user_exited:
    user=input("YOU: ")
    tokens=word_tokenize(user)
    print(tokens)
    stop_words=set(stopwords.words('english'))

    # Remove stop words from tokens
    filtered_words=[word for word in tokens if word.lower() not in stop_words]

    for word in filtered_words:
        if word in quit_statements or word in greeting_statements:
            if word.lower() in quit_statements:
                print("CHATBOT: Bye !, it was nice having you...")
                user_exited=False
            elif word.lower() in greeting_statements:
                print("CHATBOT: How can i help you")
        else:
            print("CHATBOT: Sorry !, I cant understand that ")





