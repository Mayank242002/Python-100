##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




import pandas as pd
import datetime as dt
import random
import smtplib

today=dt.datetime.now()
day=today.day
print(day)

df=pd.read_csv("Day-32-birthday-wishe/birthdays.csv")
list=df.to_dict(orient="records")
name=""
reciver_email=""

for current_dict in list:
    if (day==current_dict['day']):
        name=current_dict['name']
        reciver_email=current_dict['email']
        
      
        random_file_no=random.randint(1,3)
        file=open(f"Day-32-birthday-wishe/letter_templates/letter_{random_file_no}.txt","r")
        data=file.read()
        data=data.replace('[NAME],',name+",")
        print(data)       
            

        my_email="msngi24july@gmail.com"
    
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password="mayank@1234")
        
        connection.sendmail(
            from_addr=my_email,
            to_addrs=reciver_email,
            msg=f"Subject:Happy Birthday\n\n {data}")
           


        connection.close()





