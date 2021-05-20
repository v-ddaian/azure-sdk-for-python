# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse

from azure.maps.service.operations import TimezoneOperations
from azure.maps.service.models import ResponseFormat, TimezoneOptions
from common.common import create_maps_client


def get_timezone_by_coordinates(timezone: TimezoneOperations):
    result = timezone.get_timezone_by_coordinates(
        ResponseFormat.JSON, "47.0,-122", None, TimezoneOptions.ALL)
    print("Get Timezone By Coordinate")
    print(result)


def get_timezone_by_id(timezone: TimezoneOperations):
    result = timezone.get_timezone_by_id(
        ResponseFormat.JSON, "Asia/Bahrain", None, TimezoneOptions.ALL)
    print("Get Timezone By Id")
    print(result)


def get_timezone_enum_iana(timezone: TimezoneOperations):
    result = timezone.get_timezone_enum_iana(ResponseFormat.JSON)
    print("Get Timezone Enum IANA")
    print(result)


def get_timezone_enum_windows(timezone: TimezoneOperations):
    result = timezone.get_timezone_enum_windows(ResponseFormat.JSON)
    print("Get Timezone Enum Windows")
    print(result)


def get_timezone_iana_version(timezone: TimezoneOperations):
    result = timezone.get_timezone_iana_version(ResponseFormat.JSON)
    print("Get Timezone IANA Version")
    print(result)


def get_timezone_windows_to_iana(timezone: TimezoneOperations):
    result = timezone.get_timezone_windows_to_iana(
        ResponseFormat.JSON, "pacific standard time")
    print("Get Timezone Windows to IANA")
    print(result)


def main():
    timezone = create_maps_client().timezone
    get_timezone_by_coordinates(timezone)
    get_timezone_by_id(timezone)
    get_timezone_enum_iana(timezone)
    get_timezone_enum_windows(timezone)
    get_timezone_iana_version(timezone)
    get_timezone_windows_to_iana(timezone)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Timezone Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.parse_args()
    main()
