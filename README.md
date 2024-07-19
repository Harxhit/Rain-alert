[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![API](https://img.shields.io/badge/API-Active-blue?style=for-the-badge&logo=api&logoColor=white)](https://example.com)
[![API Developer](https://img.shields.io/badge/API%20Developer-Active-blue?style=for-the-badge&logo=api&logoColor=white)](https://example.com)






# Rain Alert 🌧️
The Rain Alert Messaging App is a Python-based application designed to notify users via SMS if there is a forecast of rain at their specified location. This app leverages weather data from the OpenWeatherMap API and sends alerts using the Twilio SMS service and whatsapps services.

## Key Features:
- Fetches weather forecast data for a specified location.
- Checks for rain conditions in the forecast.
- Sends an SMS alert to the user if rain is expected.

## Technologies Used:
### Python:
The primary programming language used for developing the application.

### Requests Library:
Used to make HTTP requests to the OpenWeatherMap API.

### OpenWeatherMap API:
Provides weather forecast data.

### Twilio API:
Facilitates sending SMS notifications.

## Detailed Breakdown:

### Importing Libraries:
- **requests**: To handle API requests to OpenWeatherMap.
- **twilio.rest.Client**: To interact with the Twilio API for sending SMS.

### Setting Up Coordinates and API Credentials:
- **Latitude and Longitude**: The geographical coordinates for the weather data.
- **api_key**: API key for accessing the OpenWeatherMap data.
- **account_sid and auth_token**: Credentials for Twilio API authentication.

### Defining Parameters for the Weather API Request:
- Parameters include latitude, longitude, API key, and the number of forecast data points (`cnt`).

### Making the Weather API Request:
- Using `requests.get()` to fetch the weather forecast data.
- Checking for a successful response with `response.raise_for_status()`.

### Processing the Weather Data:
- Parsing the JSON response to extract weather conditions.
- Checking if the weather condition code indicates rain (condition codes less than 700).

### Sending SMS Notification:
- If rain is expected, the Twilio `Client` is used to send an SMS alert and whatsapp to the user.
- The message body includes a reminder to bring an umbrella.
- If no rain is forecasted, a clear weather message is printed.

## Links 
### Open Weather  - https://openweathermap.org/
### Online JSON file reader - https://jsonviewer.stack.hu/
### Twilio - https://www.twilio.com/
### Weather - https://www.ventusky.com/?p=17.46;74.08;6&l=rain-3h
