import requests
from twilio.rest import Client
import os

# Load credentials from environment variables
Latitude = 24.530727
Longitude = 81.299110
api_key = os.getenv("WEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
my_phone_number = os.getenv("MY_PHONE_NUMBER")

# Set parameters for the API request
parameters = {
  "lat": Latitude, 
  "lon": Longitude, 
  "appid": api_key, 
  "cnt": 9
}

# Make a request to the weather API
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

# Check weather conditions
for hour_data in data["list"]:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True
        break

# Send SMS notification if it will rain
client = Client(account_sid, auth_token)
if will_rain:
    client.messages.create(
        body="It is going to rain today. Remember to bring an umbrella☂️",
        from_=twilio_phone_number,
        to=my_phone_number  # Ensure this is in E.164 format
    )
    print("Message sent successfully")
else:
    print("Weather is clear")
