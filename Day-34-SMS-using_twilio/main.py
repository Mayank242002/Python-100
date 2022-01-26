import requests
from twilio.rest import Client

API_ENDPOINT="https://api.openweathermap.org/data/2.5/onecall"
API_KEY="c330fc44a97066547ea044f31c873fde"
account_sid = 'AC71a6feda8258f6ebdb6d8d39f07f56cf'
auth_token = 'a3506abb37fcb87765df5653c5e8d303'


weather_params={
    "lat":30.222401,
    "lon":78.777100,
    "appid":API_KEY,
    "exclude":"current,minutely,daily"
}

response=requests.get(API_ENDPOINT,params=weather_params)
response.raise_for_status()
weather_data=response.json()
weather_slice=weather_data["hourly"][:12]

is_rain=False
for day in weather_slice:
    if (day["weather"][0]["id"]<700):
        is_rain=True
print(is_rain)
if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Its Going to be Rain today.Be Ready with your Umbrella",
                     from_='+16067072673',
                     to='+919027038073'
                 )

    print(message.status)

