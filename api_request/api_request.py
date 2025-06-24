import requests
import os
#from dotenv import load_dotenv
from airflow.hooks.base import BaseHook

api_conn= BaseHook.get_connection('weather_api_key')
api_key= api_conn.password
api_url= f"http://api.weatherstack.com/current?access_key={api_key}&query= London, United Kingdom"

def fetch_data():
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("request seccessfull.")
        return response.json()

        # if 'error' in data:
        #     error_info = data['error']['info']
        #     print(f"API returned an error: {error_info}")
        #     raise Exception(f"API Error: {error_info}")
        # # --- End of new code ---

        # print("Request successful and payload contains weather data.")
        # return data
    except requests.exceptions.RequestException as e:
        print(f"An error occured{e}")
        raise


fetch_data() 
# comment the actual fetch_data() and dont call it for now, so we can save api calls as we have limited api request calls
# for now we are using the below data for 'New York' city just to make our postgresql database
def moc_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-06-13 18:55', 'localtime_epoch': 1749840900, 'utc_offset': '-4.0'}, 'current': {'observation_time': '10:55 PM', 'temperature': 24, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '05:25 AM', 'sunset': '08:28 PM', 'moonrise': '10:55 PM', 'moonset': '07:01 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 97}, 'air_quality': {'co': '545.75', 'no2': '92.685', 'o3': '51', 'so2': '14.615', 'pm2_5': '51.615', 'pm10': '53.465', 'us-epa-index': '3', 'gb-defra-index': '3'}, 'wind_speed': 14, 'wind_degree': 158, 'wind_dir': 'SSE', 'pressure': 1020, 'precip': 0, 'humidity': 45, 'cloudcover': 0, 'feelslike': 25, 'uv_index': 1, 'visibility': 13, 'is_day': 'yes'}}