import smtplib
import os
import requests

onecall_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
my_api_key = "fc5b526181f341578f988874e63a0db5"

my_email = os.environ.get('MY_EMAIL')
my_pass = os.environ.get('MY_PASS')


parameters = {

    "lat": "33.720001",
    "lng": "73.059998",
    "appid":my_api_key

}
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall?lat=23&lon=90&exclude=current,minutely,daily&appid=fc5b526181f341578f988874e63a0db5"
response = requests.get(weather_endpoint)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# if will_rain:
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email,
                        to_addrs="lakho75@yahoo.com",
                        msg="Subject: Rain Alert\n\nIt's raining bring the umbrella")


print("Mail has been sent successfully!")