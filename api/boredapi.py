# boredAPI.py
import requests


def get_response(participants):
    response = requests.get(f"http://www.boredapi.com/api/activity?participants={participants}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
