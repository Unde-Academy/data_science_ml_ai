import requests

API_KEY  = '4dd2db7465869cb31168eb2a33536e9a'

#Defines the API endpoint and parameters
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
CITY_NAME = input("Enter a city name: ")

PARAMS = {
    'q': CITY_NAME,
    'appid': API_KEY,
    'units': 'metric'
}

#Make the API request
response = requests.get(BASE_URL, params=PARAMS)

#Check if the request was successful
if response.status_code == 200:

    #create a JSON response
    data = response.json()

    #Extract the weather data
    weather_desc = data ['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    #Print the weather data
    print(f"weather in {CITY_NAME}: ")
    print("Weather description:", weather_desc)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Wind speed:", wind_speed, "m/s")
else:
    print(f"failed to retrieve data. status code: {response.status_code}")
    print(f"error message: {response.text}")
