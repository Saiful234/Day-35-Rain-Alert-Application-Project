import os
import requests
import smtplib
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "AC54b0c580e051f106a1beb92bcfeb10d0"
auth_token = "96e20e75f26731c14818aa264f264985"

MY_EMAIL = "bandotech46@gmail.com"
MY_PASSWORD = "hdyfxydtypgmmvnd"

LATITUDE = 13.082680
LONGITUDE = 80.270721

api_key = "37ffe48fe89ef6d975cfaf670957b86e"
api_url = f"https://api.openweathermap.org/data/2.5/onecall"

parameter = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts",
}
response = requests.get(api_url, params=parameter)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
# weather_data["hourly"][0]["weather"][0]["id"]
hourly_data= weather_data["hourly"][:12]


will_rain = False
for id in hourly_data:
    weather_code = int(id["weather"][0]["id"])
    if weather_code < 600:
        will_rain = True

# if will_rain:
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#     client = Client(account_sid, auth_token, http_client=proxy_client)
#     message = client.messages \
#                 .create(
#                      body="It's gonna rain today, Remember to bring umbrella",
#                      from_='+15017122661',
#                      to='+919489151902'
#                  )
#     print(message.status)

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Rain Alert\n\nIt's gonna rain today, Remember to bring umbrella",
        )