import requests

API_KEY = "78d1087ca2309a67aa820b3388da051b"
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
limit = 1

city = input("Enter a city name: ")
request_geo = f"{GEO_URL}?q={city}&appid={API_KEY}"
response_geo = requests.get(request_geo)

if response_geo.status_code == 200:
    data_geo = response_geo.json()
    lat = data_geo[0]['lat']
    lon = data_geo[0]['lon']
    request_weather = f"{WEATHER_URL}?lat={lat}&lon={lon}&appid={API_KEY}"
    response_weather = requests.get(request_weather)
    if response_weather.status_code == 200:
        data_weather = response_weather.json()
        weather = data_weather['weather'][0]['main']
        temp = data_weather['main']['temp'] - 273.15
        print("Weather : ", weather)
        print("temp : ", "%.2f" % temp, "°C")
    else:
        print("An error has occured")
else:
    print("An error has occured")
