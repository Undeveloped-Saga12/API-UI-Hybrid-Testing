import requests
import logging

# initialize the logger
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
class APIClient:
    def __init__(self):
        self.base_url="https://reqres.in/api"

    def create_user(self,name,job):
        url=f"{self.base_url}/users"
        payload={"name":name,"job":job}
        # log the API request
        logger.info(f"Sending POST request(url)")
        logger.info(f"Payload:{payload}")
        response=requests.post(url,json=payload)
        response_data=response.json()

        # log the API response
        logger.info(f"Response Status Code:{response.status_code}")
        logger.info(f"API Response:{response_data}")
        
        return response_data