import requests
import datetime as dt
import os 
from dotenv import load_dotenv

load_dotenv()

SECRET_TOKEN=os.getenv('SECRET_TOKEN')
TODAY_DATE=dt.datetime.now()
API_ID=os.getenv('API_ID')
API_KEY=os.getenv('API_KEY')
headers={

    "x-app-id":API_ID,
    "x-app-key":API_KEY,
    "Content-Type": "application/json"
}
User_query=input("Enter Your Workout Details for Today:")
exercise={
 "query":User_query,
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

response1=requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",json=exercise,headers=headers)
response1.raise_for_status()
required_exercises=response1.json()["exercises"]
print(required_exercises)

for exercise in required_exercises:
    body={
    "workout":{
        "date":TODAY_DATE.strftime("%d/%m/%Y"),
        "time":TODAY_DATE.strftime("%X"),
        "exercise":exercise["name"],
        "duration":exercise["duration_min"],
        "calories":exercise["nf_calories"]
    } 
}
    new_headers={
        "Authorization":f"Bearer {SECRET_TOKEN}"
    }
    
    response2=requests.post(url="https://api.sheety.co/4a7c3a0662c9f65c530aedd86076c66d/workoutTracking/workouts",json=body,headers=new_headers)
    print(response2.json())
    


