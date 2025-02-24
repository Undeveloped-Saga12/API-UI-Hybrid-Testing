import requests

class APIClient:
    def __init__(self):
        self.base_url="https://reqres.in/api"

    def create_user(self,name,job):
        url=f"{self.base_url}/users"
        payload={"name":name,"job":job}
        response=requests.post(url,json=payload)
        return response.json()