import requests
import datetime as dt
import smtplib
import time

# Location Constants
LATITUDE = 22.7196
LONGITUDE = 75.8577

# Email Constants
email = "harsxit04@gmail.com"
password = "fkzd ghcg drzi odod"

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if LATITUDE - 5 <= iss_latitude <= LATITUDE + 5 and LONGITUDE - 5 <= iss_longitude <= LONGITUDE + 5:
        return True
    return False

def is_night():
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(email, password)
                connection.sendmail(
                    from_addr=email,
                    to_addrs=email,
                    msg="Subject:Look Up\n\nInternational Space Station is overhead, look up in the sky."
                )
            print("Email Sent")
        except Exception as e:
            print("Email Not Sent", e)
    else:
        print("Conditions not met or ISS not overhead")
