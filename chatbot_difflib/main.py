from difflib import get_close_matches
import json
from colorama import Fore,Style

def load_database(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
    
def save_to_database(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def find_best_match(user_input, questions):
    return get_close_matches(user_input, questions, 1, cutoff=0.7)

def get_chatbot_response(user_input, data):
    for question in data["Questions"]:
        if question["question"] == user_input:
            return question["answer"]
    return None

def main():
    file_path = 'chatbot_difflib//database.json'
    data = load_database(file_path)
    
    while True:
        user_input = input(f'You: {Fore.GREEN}')
        if user_input.lower() == 'exit':
            print(f'Chatbot: {Fore.GREEN}Goodbye!{Style.RESET_ALL}')
            break
        questions = [q["question"] for q in data["Questions"]]
        best_match = find_best_match(user_input, questions)
        if best_match:
            answer = get_chatbot_response(best_match[0], data)
            print(f"{Style.RESET_ALL}"f"Chatbot: {Fore.GREEN}{answer}{Style.RESET_ALL}")
        else:
            print(f"{Style.RESET_ALL}"f"Chatbot: {Fore.GREEN }I'm not sure, but I can tell you that it's not possible to answer this question.{Style.RESET_ALL}")
            new_answer = input("Type the answer or just 'skip': ")
            if new_answer.lower() != 'skip':
                data["Questions"].append({"question": user_input, "answer": new_answer})
                save_to_database(file_path, data)
            else:
                break
           
    print(data["Questions"])
if __name__ == "__main__":
    main()
 

