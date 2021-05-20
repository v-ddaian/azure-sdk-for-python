# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse

from azure.maps.service.operations import ElevationOperations
from azure.maps.service.models import ResponseFormat, CoordinatesPairAbbreviated

from common.common import create_maps_client


def get_data_for_bounding_box(elevation: ElevationOperations):
    result = elevation.get_data_for_bounding_box(ResponseFormat.JSON, [
                                                 "-121.66853362143818", "46.84646479863713", "-121.65853362143818", "46.85646479863713"], rows=3, columns=3)
    print("Get Data for bounding box")
    print(result)
    print("Data array:")
    for point_result in result.data:
        print(point_result)


def get_data_for_point(elevation: ElevationOperations):
    result = elevation.get_data_for_points(ResponseFormat.JSON, [
                                           "-121.66853362143818,46.84646479863713", "-121.65853362143818,46.85646479863713"])
    print("Get Data for points")
    print(result)
    print("Data array:")
    for point_result in result.data:
        print(point_result)


def get_data_for_polyline(elevation: ElevationOperations):
    result = elevation.get_data_for_polyline(ResponseFormat.JSON, [
                                             "-121.66853362143818,46.84646479863713", "-121.65853362143818,46.85646479863713"])
    print("Get Data for polyline")
    print(result)
    print("Data array:")
    for point_result in result.data:
        print(point_result)


def post_data_for_points(elevation: ElevationOperations):
    coord1 = CoordinatesPairAbbreviated(
        lat=46.84646479863713, lon=-121.66853362143818)
    coord2 = CoordinatesPairAbbreviated(
        lat=46.856464798637127, lon=-121.68853362143818)
    result = elevation.post_data_for_points(
        ResponseFormat.JSON, [coord1, coord2])
    print("Get Data for multiple points")
    print(result)
    print("Data array:")
    for point_result in result.data:
        print(point_result)


def post_data_for_polyline(elevation: ElevationOperations):
    coord1 = CoordinatesPairAbbreviated(
        lat=46.84646479863713, lon=-121.66853362143818)
    coord2 = CoordinatesPairAbbreviated(
        lat=46.856464798637127, lon=-121.68853362143818)
    result = elevation.post_data_for_polyline(
        ResponseFormat.JSON, [coord1, coord2])
    print("Get Data for long polyline")
    print(result)
    print("Data array:")
    for point_result in result.data:
        print(point_result)


def main():
    elevation = create_maps_client().elevation
    get_data_for_bounding_box(elevation)
    get_data_for_point(elevation)
    get_data_for_polyline(elevation)
    post_data_for_points(elevation)
    post_data_for_polyline(elevation)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Elevation Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.parse_args()
    main()
