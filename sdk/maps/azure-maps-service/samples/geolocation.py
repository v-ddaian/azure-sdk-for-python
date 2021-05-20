# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse

from azure.maps.service.operations import GeolocationOperations
from azure.maps.service.models import ResponseFormat

from common.common import create_maps_client


def get_ip_to_location_preview(geolocation: GeolocationOperations, ip: str):
    result = geolocation.get_ip_to_location_preview(ResponseFormat.JSON, ip)
    print("Got location by ip")
    print(result)
    print(result.country_region)


def main(ip: str):
    geolocation = create_maps_client().geolocation
    get_ip_to_location_preview(geolocation, ip)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Geolocation Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.add_argument('--ip', action="store", required=True)
    main(parser.parse_args().ip)
