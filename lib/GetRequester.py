import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Return the response as raw bytes

    def load_json(self):
        response_body = self.get_response_body()
        return requests.get(self.url).json()  # Convert the response to JSON and return as Python list
    
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(get_requester.load_json())
