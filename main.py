
import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
my_api = "fc5b526181f341578f988874e63a0db5"

parameters = {
    "lat": 24.860735,
    "lng": 67.001137,
    "appid": my_api,
}


end_point = "https://api.openweathermap.org/data/2.5/onecall?lat=24.860735&lon=67.001137&exclude=current,minutely,daily&appid=fc5b526181f341578f988874e63a0db5"
response = requests.get(end_point)
response.raise_for_status()

weather_data = response.json()
# print(weather_data)
hourly_data = weather_data['hourly']
weather_id = weather_data['hourly'][1]['weather'][0]['id']

will_not_rain = True
for item in hourly_data[0:12]:
    if weather_id <= 700:
        will_not_rain = False

else:
    print("No need to bring the umbrella")

