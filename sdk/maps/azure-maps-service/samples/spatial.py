# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse
import json
import datetime

from azure.maps.service.operations import SpatialOperations
from azure.maps.service.models import TextFormat, GeofenceMode

from common.common import create_maps_client


def get_buffer(spatial: SpatialOperations, udid: str):
    result = spatial.get_buffer(TextFormat.JSON, udid, "176.3")
    print("Get Buffer")
    print(result)


def get_closest_point(spatial: SpatialOperations, udid: str):
    result = spatial.get_closest_point(
        TextFormat.JSON, udid, 47.622942, -122.316456)
    print("Get Closest Point")
    print(result)


def get_geofence(spatial: SpatialOperations, udid: str, device_id: str):
    result = spatial.get_geofence(TextFormat.JSON, device_id, udid, 48.36, -124.63, None,
                                  datetime.datetime(2018, 9, 9, 10, 0, 0), 50, False, GeofenceMode.ENTER_AND_EXIT)
    print("Get Geofence")
    print(result)


def get_great_circle_distance(spatial: SpatialOperations):
    result = spatial.get_great_circle_distance(
        TextFormat.JSON, "47.622942,-122.316456:47.610378,-122.200676")
    print("Get Great Circle Distance")
    print(result)


def get_point_in_polygon(spatial: SpatialOperations, udid: str):
    result = spatial.get_point_in_polygon(
        TextFormat.JSON, udid, 47.622942, -122.316456)
    print("Get Point In Polygon")
    print(result)


def post_buffer(spatial: SpatialOperations):
    with open("resources/spatial_buffer_request_body.json", "r") as file:
        result = spatial.post_buffer(TextFormat.JSON, json.loads(file.read()))
        print("Post Buffer")
        print(result)


def post_closest_point(spatial: SpatialOperations):
    with open("resources/spatial_closest_point_request_body.json", "r") as file:
        result = spatial.post_closest_point(
            TextFormat.JSON, 47.622942, -122.316456, json.loads(file.read()))
        print("Post Closest Point")
        print(result)


def post_geofence(spatial: SpatialOperations, device_id: str):
    with open("resources/spatial_geofence_request_body.json", "r") as file:
        result = spatial.post_geofence(TextFormat.JSON, device_id, 48.36, -124.63, json.loads(
            file.read()), None, datetime.datetime(2018, 9, 9, 10, 0, 0), 50, False, GeofenceMode.ENTER_AND_EXIT)
        print("Post Geofence")
        print(result)


def post_point_in_polygon(spatial: SpatialOperations, udid: str, device_id: str):
    with open("resources/spatial_geofence_request_body.json", "r") as file:
        result = spatial.post_point_in_polygon(
            TextFormat.JSON, 48.36, -124.63, json.loads(file.read()))
        print("Post Point In Polygon")
        print(result)


def main(udid: str, device_id: str):
    spatial = create_maps_client().spatial
    get_buffer(spatial, udid)
    get_closest_point(spatial, udid)
    get_geofence(spatial, udid, device_id)
    get_great_circle_distance(spatial)
    get_point_in_polygon(spatial, udid)
    post_buffer(spatial)
    post_closest_point(spatial)
    post_geofence(spatial, device_id)
    post_point_in_polygon(spatial, udid, device_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Spatial Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.add_argument('--udid', action="store", required=True)
    parser.add_argument('--device_id', action="store", required=True)
    main(parser.parse_args().udid, parser.parse_args().device_id)
