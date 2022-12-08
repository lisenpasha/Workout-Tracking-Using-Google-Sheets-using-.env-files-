import requests
from datetime import datetime
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
username=os.getenv("username")
GENDER = "male"
WEIGHT_KG = "97"
HEIGHT_CM = "186"
AGE = "23"

APP_ID=os.getenv("APP_ID")
API_KEY=os.getenv("API_KEY")
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}
x=input("Tell me which exercises you did: ")
body_params={
 "query":x,
 "gender":GENDER,
 "weight_kg":WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age":AGE
}

response=requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",json=body_params,params=headers)
result=response.json()
print(result)

sheet_endpoint="https://api.sheety.co/fba4fbf2157683945e73735e884e6d0f/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
headers_2={
    "Authentication":os.getenv("Authentication")
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers_2)
    sheet_response={}

