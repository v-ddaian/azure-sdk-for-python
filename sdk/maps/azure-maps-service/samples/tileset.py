# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse
from typing import List
from azure.maps.service import operations

from azure.maps.service.operations import TilesetOperations
from azure.maps.service.models import TilesetDetailInfo
from azure.core.exceptions import HttpResponseError
from common.common import create_maps_client, get_operation_location_id, wait_for_status_complete


def create(tileset: TilesetOperations, dataset_id: str):
    poller = tileset.begin_create(dataset_id, "Test Description", polling=False)
    operation_id = get_operation_location_id(poller, "operation-location")
    print("Created tileset with operation_id {}".format(operation_id))
    return operation_id


def delete(tileset: TilesetOperations, tileset_id: str):
    tileset.delete(tileset_id)
    print("Deleted tileset with tilesetId {}".format(tileset_id))


def get(tileset: TilesetOperations, tileset_id: str):
    result = tileset.get(tileset_id)
    print("Get tileset with tilesetId {}".format(tileset_id))
    print(result)


def get_operation(tileset: TilesetOperations, operation_id: str):
    result = tileset.get_operation(operation_id)
    print("Get tileset with operation_id {}".format(operation_id))
    print(result)
    return result


def list(tileset: TilesetOperations):
    result = tileset.list()
    tilesets: List[TilesetDetailInfo] = result.tilesets
    print("View all tilesets:")
    for tileset_info in tilesets:
        print(tileset_info)


def main(dataset_id: str):
    tileset = create_maps_client().tileset
    operation_id = create(tileset, dataset_id)
    tileset_id = wait_for_status_complete(tileset, operation_id, get_operation)
    if tileset_id is None:
        print("Tileset creation faled")
        return
    try:
        get(tileset, tileset_id)
        list(tileset)
    except HttpResponseError as e:
        print(e)
    finally:
        delete(tileset, tileset_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Tileset Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.add_argument('--dataset_id', action="store", required=True)
    main(parser.parse_args().dataset_id)
