# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse
import pprint
import json

from azure.maps.service.operations import SearchOperations
from azure.maps.service.models import TextFormat

from common.common import create_maps_client
from typing import List

pp = pprint.PrettyPrinter(indent=4)


def get_search_address(search: SearchOperations):
    result = search.get_search_address(
        TextFormat.JSON, "15127 NE 24th Street, Redmond, WA 98052")
    print("Get Search Address:")
    print(result)


def get_search_address_reverse(search: SearchOperations):
    result = search.get_search_address_reverse(
        TextFormat.JSON, "37.337,-121.89")
    print("Get Search Address Reverse:")
    print(result)


def get_search_address_reverse_cross_street(search: SearchOperations):
    result = search.get_search_address_reverse_cross_street(
        TextFormat.JSON, "37.337,-121.89")
    print("Get Search Address Reverse Cross Street:")
    print(result)


def get_search_address_structured(search: SearchOperations):
    result = search.get_search_address_structured(
        TextFormat.JSON, None, "US", None, None, 15127, "NE 24th Street", None, "Redmond", None, None, None, "WA", "98052")
    print("Get Search Address Structured:")
    print(result)


def get_search_fuzzy(search: SearchOperations):
    results = search.get_search_fuzzy(TextFormat.JSON, "seattle")
    print("Get Search Fuzzy:")
    print(results)
    return list(map(lambda result: result.data_sources.geometry.id, results.results))


def get_search_nearby(search: SearchOperations):
    result = search.get_search_nearby(
        TextFormat.JSON, 40.706270, -74.011454, 10, None, None, None, 8046)
    print("Get Search Fuzzy:")
    print(result)


def get_search_poi(search: SearchOperations):
    result = search.get_search_poi(
        TextFormat.JSON, "juice bars", None, 5, None, None, None, 47.606038, -122.333345, 8046)
    print("Get Search POI:")
    print(result)


def get_search_poi_category(search: SearchOperations):
    result = search.get_search_poi_category(
        TextFormat.JSON, "atm", None, 5, None, None, None, 47.606038, -122.333345, 8046)
    print("Get Search POI Category:")
    print(result)


def get_search_poi_category_tree(search: SearchOperations):
    result = search.get_search_poi_category_tree_preview(TextFormat.JSON)
    print("Get Search POI Category Tree:")
    print(result)


def get_search_polygon(search: SearchOperations, ids: List[str]):
    result = search.get_search_polygon(TextFormat.JSON, ids)
    print("Get Search Polygon:")
    print(result)


def post_search_address_batch(search: SearchOperations):
    with open("resources/search_address_batch_request_body.json", "r") as file:
        poller = search.begin_post_search_address_batch(
            TextFormat.JSON, json.loads(file.read()), polling_interval=5)
        result = poller.result()
        print("Post Search Address Batch")
        print(result)


def post_search_address_reverse_batch(search: SearchOperations):
    with open("resources/search_address_reverse_batch_request_body.json", "r") as file:
        poller = search.begin_post_search_address_reverse_batch(
            TextFormat.JSON, json.loads(file.read()), polling_interval=5)
        result = poller.result()
        print("Post Search Address Reverse Batch")
        print(result)


def post_search_fuzzy_batch(search: SearchOperations):
    with open("resources/search_fuzzy_batch_request_body.json", "r") as file:
        poller = search.begin_post_search_fuzzy_batch(
            TextFormat.JSON, json.loads(file.read()), polling_interval=5)
        result = poller.result()
        print("Post Search Fuzzy Batch")
        print(result)


def post_search_along_route(search: SearchOperations):
    with open("resources/search_along_route_request_body.json", "r") as file:
        result = search.post_search_along_route(
            TextFormat.JSON, "burger", 1000, json.loads(file.read()), limit=2)
        print("Post Search Along Route")
        print(result)


def post_search_inside_geometry(search: SearchOperations):
    with open("resources/search_inside_geometry_request_body.json", "r") as file:
        result = search.post_search_inside_geometry(
            TextFormat.JSON, "burger", json.loads(file.read()), limit=2)
        print("Post Search Inside Geometry")
        print(result)


def main():
    search = create_maps_client().search
    get_search_address(search)
    get_search_address_reverse(search)
    get_search_address_reverse_cross_street(search)
    get_search_address_structured(search)
    ids = get_search_fuzzy(search)
    get_search_nearby(search)
    get_search_poi(search)
    get_search_poi_category(search)
    get_search_poi_category_tree(search)
    get_search_polygon(search, ids)
    post_search_address_batch(search)
    post_search_address_reverse_batch(search)
    post_search_fuzzy_batch(search)
    post_search_along_route(search)
    post_search_inside_geometry(search)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Search Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.parse_args()
    main()
