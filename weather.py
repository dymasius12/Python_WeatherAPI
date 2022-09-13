import requests


API_KEY = "c1fb755a8d70f4cd9ff809c3359c0a3e"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
