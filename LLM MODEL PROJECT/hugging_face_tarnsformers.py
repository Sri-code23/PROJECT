#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

import requests

token_access=" "
API_URL=" "
headers= {"Authorisation": f"Bearer{token_access}"}

response = requests.request("POST" , API_URL, headers=headers , data=data)

print(response.json())