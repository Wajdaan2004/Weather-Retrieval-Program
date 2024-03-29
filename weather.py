import requests

API_KEY = "bdeb87b1c346e73dc31bf6c726da019c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather'][0]['description']
    temperature = round((data["main"]["temp"])-273.15,2)
    feels = round((data["main"]["feels_like"])-273.15)
    wind = data["wind"]["speed"]
    wind_feels = "Light"

    if wind >= 11:
        wind_feels = "Strong"

    print ("Weather:", weather)
    print ("Temperature:", temperature, "celsius")
    print ("Feels like: ", feels, "celsius")
    print ("Winds:", wind_feels)
else:
    print("error")