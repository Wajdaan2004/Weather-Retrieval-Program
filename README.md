Weather API Python Client
This Python script is a simple command-line client for retrieving weather information using the OpenWeatherMap API. It takes a user-provided city name as input and fetches the current weather data, including temperature, weather description, and wind information.

Requirements
Python 3.x
Requests library (install using "pip install requests")
OpenWeatherMap API Key
Usage
Run the script using a command like python weather_client.py.
Enter the name of the city when prompted.
The script will make an API call to OpenWeatherMap, process the response, and display relevant weather information.
Configuration
Make sure to replace the placeholder API_KEY with your actual OpenWeatherMap API key.
The base URL for OpenWeatherMap API is set to "http://api.openweathermap.org/data/2.5/weather".
You may need to sign up for an API key at OpenWeatherMap to use this script.

Notes
The script converts temperatures from Kelvin to Celsius.
Wind speed is categorized as "Light" or "Strong" based on a threshold of 11 m/s.

README.md

Weather API Python Client
This Python script fetches current weather information using the OpenWeatherMap API.

Getting Started
Clone the repository: git clone [repository URL]
Install required dependencies: pip install -r requirements.txt
Obtain an API key from OpenWeatherMap and replace the placeholder in the script with your key.
Usage
Run the script and enter a city name when prompted.
