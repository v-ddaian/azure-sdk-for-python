# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse

from azure.maps.service.operations import WeatherOperations
from azure.maps.service.models import ResponseFormat
from common.common import create_maps_client


def get_current_conditions(weather: WeatherOperations):
    result = weather.get_current_conditions(
        ResponseFormat.JSON, "47.641268,-122.125679")
    print("Get Current Conditions")
    print(result)


def get_daily_forecast(weather: WeatherOperations):
    result = weather.get_daily_forecast(
        ResponseFormat.JSON, "62.6490341,30.0734812", duration=5)
    print("Get Daily Forecast")
    print(result)


def get_daily_indices(weather: WeatherOperations):
    result = weather.get_daily_indices(
        ResponseFormat.JSON, "43.84745,-79.37849", index_group_id=11)
    print("Get Daily Indices")
    print(result)


def get_hourly_forecast(weather: WeatherOperations):
    result = weather.get_hourly_forecast(
        ResponseFormat.JSON, "47.632346,-122.138874", duration=12)
    print("Get Hourly Forecast")
    print(result)


def get_minute_forecast(weather: WeatherOperations):
    result = weather.get_minute_forecast(
        ResponseFormat.JSON, "47.632346,-122.138874", interval=15)
    print("Get Minute Forecast")
    print(result)


def get_quarter_day_forecast(weather: WeatherOperations):
    result = weather.get_quarter_day_forecast(
        ResponseFormat.JSON, "47.632346,-122.138874", duration=1)
    print("Get Quarter Day Forecast")
    print(result)


def get_severe_weather_alerts(weather: WeatherOperations):
    result = weather.get_severe_weather_alerts(
        ResponseFormat.JSON, "48.057,-81.091")
    print("Get Severe Weather Alerts")
    print(result)


def get_weather_along_route(weather: WeatherOperations):
    result = weather.get_weather_along_route(
        ResponseFormat.JSON, "38.907,-77.037,0:38.907,-77.009,10:38.926,-76.928,20:39.033,-76.852,30:39.168,-76.732,40:39.269,-76.634,50:39.287,-76.612,60")
    print("Get Weather Along Route")
    print(result)


def main():
    weather = create_maps_client().weather
    get_current_conditions(weather)
    get_daily_forecast(weather)
    get_daily_indices(weather)
    get_hourly_forecast(weather)
    get_minute_forecast(weather)
    get_quarter_day_forecast(weather)
    get_severe_weather_alerts(weather)
    get_weather_along_route(weather)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Weather Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.parse_args()
    main()
