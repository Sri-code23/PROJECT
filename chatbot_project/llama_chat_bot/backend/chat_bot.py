#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

import requests

# Your Hugging Face API token (replace 'YOUR_HF_API_TOKEN' with your actual token)
API_TOKEN = "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"

# The Hugging Face API URL for the model (you can use a lightweight LLaMA variant here)
API_URL = "https://api-inference.huggingface.co/models/openlm-research/open_llama_7b"

# Headers including the token
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def generate_response(prompt):
    payload = {
        "inputs": prompt
    }

    # Send the POST request to Hugging Face Inference API
    response = requests.post(API_URL, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"]
    else:
        return f"Error {response.status_code}: {response.text}"

if __name__ == "__main__":
    # Take user input
    prompt = input("You: ")

    # Generate and print chatbot response
    response = generate_response(prompt)
    print(f"Bot: {response}")
