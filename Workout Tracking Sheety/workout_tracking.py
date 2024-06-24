from os import getenv
import requests
from datetime import datetime

# https://sheety.co O site que serve para brincar com os sheets do Google, todas as informações estão no ep 335

APP_ID: str = getenv('application_id_nutritionix')
API_KEY: str = getenv('api_key_nutritionix')
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
GENDER = 'Male'
WEIGHT_KG = 70
HEIGHT_CM = 180
AGE = 22

parameters_nlp: dict = {
    'query': input('Tell me, which exercise you did: '),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers: dict = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    "Content-Type": "application/json",
}

response = requests.post(NUTRITIONIX_ENDPOINT, json=parameters_nlp, headers=headers)
result: list = response.json()['exercises']

URL_SHEETY: str = 'https://api.sheety.co/8b7e60d13c620b9438e6355ca1c56375/cópiaDeMyWorkouts/workouts'
bearer_headerss: dict = {"Authorization": f"Bearer {getenv('token_sheety')}"}

for exercise in result:
    sheet_inputs = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(URL_SHEETY, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
