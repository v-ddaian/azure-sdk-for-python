# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse
import json

from azure.maps.service.operations import RouteOperations
from azure.maps.service.models import TextFormat, RouteType

from common.common import create_maps_client


def get_route_directions(route: RouteOperations):
    result = route.get_route_directions(
        TextFormat.JSON, "52.50931,13.42936:52.50274,13.43872")
    print("Get route directions")
    print(result)


def get_route_range(route: RouteOperations):
    result = route.get_route_range(
        TextFormat.JSON, "50.97452,5.86605", time_budget_in_sec=6000)
    print("Get route range")
    print(result)


def post_route_directions(route: RouteOperations):
    with open("resources/route_directions_request_body.json") as file:
        result = route.post_route_directions(
            TextFormat.JSON, "52.50931,13.42936:52.50274,13.43872", json.loads(file.read()))
        print("Post route directions")
        print(result)
        for route in result.routes:
            print(route)


def post_route_directions_batch(route: RouteOperations):
    with open("resources/route_directions_batch_request_body.json") as file:
        poller = route.begin_post_route_directions_batch(
            TextFormat.JSON, json.loads(file.read()), polling=True, polling_interval=5)
        print("Post route directions batch")
        print(poller.result())


def post_route_matrix(route: RouteOperations):
    with open("resources/route_matrix_request_body.json") as file:
        poller = route.begin_post_route_matrix(
            TextFormat.JSON, json.loads(file.read()), route_type=RouteType.SHORTEST, wait_for_results=True)
        print("Post route matrix")
        print(poller.result())


def main():
    route = create_maps_client().route
    get_route_directions(route)
    get_route_range(route)
    post_route_directions(route)
    post_route_directions_batch(route)
    post_route_matrix(route)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Route Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.parse_args()
    main()
