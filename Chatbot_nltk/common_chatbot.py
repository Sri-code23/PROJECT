from fuzzywuzzy import fuzz
from nltk.tokenize import word_tokenize
import nltk
import random

# Download the required NLTK data
nltk.download('punkt')

# Define lists of greetings, goodbyes, introductions, and name responses
greetings = ["hello", "hi", "hey", "greetings"]
good_byes = ["bye", "seeyou", "see you", "goodbye"]
introductions = ["what is your name", "who are you", "name please"]
name_responses = ["my name is chatbot", "i am chatbot", "chatbot is my name"]

# Define a function to check if the user's input is a greeting
def check_greeting(user_input):
    # Iterate over each greeting and calculate the similarity ratio
    for greeting in greetings:
        # If the similarity ratio is greater than 80, return a random greeting response
        if fuzz.ratio(user_input.lower(), greeting) > 80:
            return random.choice(["hello", "hey", "hi"])

# Define a function to check if the user's input is a goodbye
def check_goodbye(user_input):
    # Iterate over each goodbye and calculate the similarity ratio
    for goodbye in good_byes:
        # If the similarity ratio is greater than 80, return a random goodbye response
        if fuzz.ratio(user_input.lower(), goodbye) > 80:
            return random.choice(["bye", "good bye", "see you"])

# Define a function to check if the user's input is an introduction
def check_introduction(user_input):
    # Iterate over each introduction and calculate the similarity ratio
    for introduction in introductions:
        # If the similarity ratio is greater than 80, return a random name response
        if fuzz.ratio(user_input.lower(), introduction) > 80:
            return random.choice(name_responses)

# Define a function to extract the user's name from their input
def get_name(user_input):
    # Tokenize the user's input into individual words
    words = word_tokenize(user_input)
    # Iterate over each word and check if it's not a greeting, goodbye, or introduction
    for word in words:
        if word.lower() not in greetings and word.lower() not in good_byes and word.lower() not in introductions:
            # Return the word as the user's name
            return word

# Define the main chatbot function
def chatbot():
    # Initialize the user's name to None
    user_name = None
    # Enter an infinite loop to continuously prompt the user for input
    while True:
        # Get the user's input
        user_input = input("User: ")
        # If the user's name is not set
        if user_name is None:
            # Check if the user's input is a greeting
            if check_greeting(user_input):
                # Print a random greeting response
                print("Chatbot: ", check_greeting(user_input))
            # Check if the user's input is an introduction
            elif check_introduction(user_input):
                # Print a random name response
                print("Chatbot: ", check_introduction(user_input))
                # Extract the user's name from their input
                user_name = get_name(user_input)
            # If the user's input is neither a greeting nor an introduction
            else:
                # Print a prompt to greet or introduce themselves
                print("Chatbot: Please greet me or introduce yourself.")
        # If the user's name is set
        else:
            # Check if the user's input is a goodbye
            if check_goodbye(user_input):
                # Print a random goodbye response
                print("Chatbot: ", check_goodbye(user_input))
                # Break out of the loop to end the chat
                break
            # If the user's input is not a goodbye
            else:
                # Print a greeting with the user's name and a prompt to ask for assistance
                print("Chatbot: Hello ", user_name, ". How can I assist you today?")

# Call the chatbot function to start the chat
chatbot()