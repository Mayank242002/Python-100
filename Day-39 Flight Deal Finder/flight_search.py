from flight_data import FlightData
from email import header
import requests

API_KEY1="84Lc9NvcYxqrftqBfsdgYI1xLMI2vpWs"
URL="https://tequila-api.kiwi.com/locations/query"
API_KEY2="D9ndPZivR83fzufC2lbWgMvnZbKlfvK9"
API_ENDPOINT2="https://tequila-api.kiwi.com/v2/search"

class FlightSearch:
    def __init__(self):
        pass

    def get_codes_for_city(self,city_name):
        headers={
    "apikey":API_KEY1
    }
        query={"term":city_name,"locale":"en-US","location-types":"city"}
        response=requests.get(url=URL,params=query,headers=headers)
        code=response.json()["locations"][0]["code"]
        return code
    
    def check_flights(self,origin_city_code,destination_city_code,from_time,to_time):
        headers={
            "apikey":API_KEY2
        }
        query={
            "fly_from":origin_city_code,
            "fly_to":destination_city_code,
            "date_from":from_time.strftime("%d/%m/%Y"),
            "date_to":to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "flight_type":"round",
            "one_for_city":1,
            "curr":"GBP"
        }

        response=requests.get(url=API_ENDPOINT2,params=query,headers=headers)
        price_array=response.json()["data"]
        if (len(price_array)!=0):

            flight_data=FlightData(price=price_array[0]["price"],
            origin_city=price_array[0]["route"][0]["cityFrom"],
            origin_airport=price_array[0]["route"][0]["flyFrom"],
            destination_city=price_array[0]["route"][0]["cityTo"],
            destination_airport=price_array[0]["route"][0]["flyTo"],
            out_date=price_array[0]["route"][0]["local_departure"].split("T")[0],
            return_date=price_array[0]["route"][1]["local_departure"].split("T")[0]
           )
            
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
        else:
            return 0



        

    
        
