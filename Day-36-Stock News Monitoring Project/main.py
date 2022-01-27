import requests
import datetime as dt
from twilio.rest import Client

now=dt.datetime.today()
today_day=now.day
account_sid = 'AC71a6feda8258f6ebdb6d8d39f07f56cf'
auth_token = '4c57c7916bc12af9f2c4596e9f5bdb2d'
API_KEY_NEWS='5846b01ece054be28519830ae020aeb4'
API_KEY_PRICE='1QodpcI40_I9bYucQpeMiuRUPZi_mStX'

response1=requests.get(f'https://api.polygon.io/v1/open-close/TSLA/2022-01-{today_day-1}?adjusted=true&apiKey={API_KEY_PRICE}')
yesterday_stock_value=response1.json()["close"]
print(yesterday_stock_value)

response2=requests.get(f'https://api.polygon.io/v1/open-close/TSLA/2022-01-{today_day-2}?adjusted=true&apiKey={API_KEY_PRICE}')
day_before_yesterday_stock_value=response2.json()["close"]
print(day_before_yesterday_stock_value)

margin=float(yesterday_stock_value-day_before_yesterday_stock_value)
logo=""
if margin>=0:
    logo='🔺'
else:
    logo='🔻'

percentage=round((abs(margin)/yesterday_stock_value)*100)

if (percentage>=1):
    response3=requests.get(f'https://newsapi.org/v2/everything?q=tesla&sortBy=popularity&apiKey={API_KEY_NEWS}')
    articles=response3.json()["articles"][0:3]
    print(articles)

    client = Client(account_sid, auth_token)
    for article in articles:
        article_heading=article["title"]
        article_description=article["description"]
        message = client.messages \
                .create(
                     body=f"TSLA: {logo}{percentage}%\n Headline: {article_heading}.\n Brief: {article_heading}.",
                     from_='+16067072673',
                     to='+919027038073'
                 )

        print(message.status)
 

       