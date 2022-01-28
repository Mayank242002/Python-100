import requests
import datetime as dt

TOKEN="Helloimmayank"
USERNAME="mayank24"

user_params={
    "token":"Helloimmayank",
    "username":"mayank24",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}

'''response=requests.post(url="https://pixe.la/v1/users",json=user_params)
print(response.text)'''

graph_config={
    "id": "graph1",
    "name":"Reading Graph",
    "unit": "commit",
    "type":"int",
    "color":"ajisai"
}

GRAPH_ID=graph_config["id"]
 
headers={
    "X-USER-TOKEN":TOKEN
}
'''response=requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs", json=graph_config,headers=headers)
print(response.text)'''

now=dt.datetime.now()

pixel_config={
    "date":now.strftime("%Y%m%d"),
    "quantity":str(input("How Many Pages Do you read Today?:"))
}


DATE=pixel_config["date"]

response=requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}",json=pixel_config,headers=headers)
print(response.text)
update_config={
    "quantity":"15"
}

'''response=requests.put(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{DATE}",json=update_config,headers=headers)
print(response.text)'''