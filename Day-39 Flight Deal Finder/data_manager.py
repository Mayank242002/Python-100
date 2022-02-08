from wsgiref import headers
import requests
from pprint import pprint

API_ENDPOINT="https://api.sheety.co/4a7c3a0662c9f65c530aedd86076c66d/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data=""

    def get_destination_data(self):
        response=requests.get(url=API_ENDPOINT)
        self.destination_data=response.json()["prices"]
        return self.destination_data
 
    def update_google_sheet(self):
        headers={

        }
        for each_city in self.destination_data:
            id=each_city["id"]
            body={
                "price":{
                    "iataCode": each_city["iataCode"]
                }
            }
            
            response=requests.put(url=f"{API_ENDPOINT}/{id}",json=body)
            print(response.status_code)

    
        

