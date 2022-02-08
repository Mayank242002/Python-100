from twilio.rest import Client

ACCOUNT_SID="AC71a6feda8258f6ebdb6d8d39f07f56cf"
AUTH_TOKEN="49bed65c9fa227c66e69ccbc75723ac8"
PHONE="+16067072673"

class NotificationManager:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self,price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        message = self.client.messages \
                .create(
                     body=f"Low Price Alert! Only £{price} to fly from LONDON-STN to {destination_city}-{destination_airport}, from {out_date} to {return_date}.",
                     from_=PHONE,
                     to='+919027038073'
                 )

        print(message.sid)