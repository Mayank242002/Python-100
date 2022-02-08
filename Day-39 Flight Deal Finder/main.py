#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime,timedelta

datamanager=DataManager()
sheet_data=datamanager.get_destination_data()
flight_search=FlightSearch()
NotificationManager=NotificationManager()

if sheet_data[0]["iataCode"]=="":
    
    for city in sheet_data:
        city["iataCode"]=flight_search.get_codes_for_city(city["city"])
    datamanager.destination_data=sheet_data
    datamanager.update_google_sheet()

tomorrow=datetime.now()+timedelta(days=1)
six_months_from_today=datetime.now()+timedelta(days=(6*30))


for destination in sheet_data:
    each_flight=flight_search.check_flights("LON",destination["iataCode"],from_time=tomorrow,to_time=six_months_from_today)
    
    if (each_flight!=0):
        if (each_flight.price<destination["lowestPrice"]):
            NotificationManager.send_sms(each_flight.price,each_flight.destination_city,each_flight.destination_airport,each_flight.destination_city,each_flight.destination_airport,each_flight.out_date,each_flight.return_date)



