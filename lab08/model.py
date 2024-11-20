import requests

NASA_API_KEY = "twG60fzhiDt4hb7oLvwSquSXlC7iY6RhBv0BYZTD"
NASA_API_URL = "https://api.nasa.gov/planetary/apod"

def get_apod_data(apod_date=None):
    params = {"api_key": NASA_API_KEY}
    if apod_date:
        params["date"] = apod_date
    response = requests.get(NASA_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")
