# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse
from typing import List

from azure.maps.service.operations import DatasetOperations
from azure.maps.service.models import DatasetDetailInfo
from azure.core.exceptions import HttpResponseError
from common.common import create_maps_client, get_operation_location_id, wait_for_status_complete


def create(dataset: DatasetOperations, conversion_id: str):
    poller = dataset.begin_create(conversion_id)
    operation_id = get_operation_location_id(poller, "operation-location")
    print("Created dataset with operation_id {} conversion_id {}".format(
        operation_id, conversion_id))
    return operation_id


def list(dataset: DatasetOperations):
    datasets = dataset.list()
    print("View all previously created datasets:")
    for dataset_list_item in datasets:
        print(dataset_list_item)


def delete(dataset: DatasetOperations, dataset_id: str):
    dataset.delete(dataset_id)
    print("Deleted dataset with id {}".format(dataset_id))


def get(dataset: DatasetOperations, dataset_id: str):
    result = dataset.get(dataset_id)
    print("Get dataset with id {}".format(dataset_id))
    print(result)


def get_operation(dataset: DatasetOperations, operation_id: str):
    result = dataset.get_operation(operation_id)
    print("Get dataset operation with id {}".format(operation_id))
    print(result)
    return result


def main(conversion_id: str, do_delete: bool):
    dataset = create_maps_client().dataset
    operation_id = create(dataset, conversion_id)
    dataset_id = wait_for_status_complete(dataset, operation_id, get_operation)
    if not dataset_id:
        print("Dataset creation faled")
        return
    try:
        list(dataset)
        get(dataset, dataset_id)
    except HttpResponseError as e:
        print(e)
    finally:
        if do_delete:
            delete(dataset, dataset_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Dataset Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.add_argument('--conversion_id', action="store", required=True)
    parser.add_argument('--dont_delete',
                        action="store_true", default=False)
    main(parser.parse_args().conversion_id, not parser.parse_args().dont_delete)
