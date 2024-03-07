import requests
from flaskApp import get_answer_endpoint
url = 'http://localhost:5000/get_answer'
data = {'user_input': 'Show me how many users have Netflix subscription?'}

response = requests.post(url, json=data)
print(response)  # Output: {'answer': 'Paris'}