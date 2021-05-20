# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse

from azure.maps.service.operations import WFSOperations
from common.common import create_maps_client


def delete_feature(wfs: WFSOperations, dataset_id: str):
    wfs.delete_feature(dataset_id, "facility", "FCL39")
    print("Delete Feature")


def get_collection(wfs: WFSOperations, dataset_id: str):
    result = wfs.get_collection(dataset_id, "facility")
    print("Get Collection")
    print(result)


def get_collection_definition(wfs: WFSOperations, dataset_id: str):
    result = wfs.get_collection_definition(dataset_id, "facility")
    print("Get Collection Definition")
    print(result)


def get_collections(wfs: WFSOperations, dataset_id: str):
    result = wfs.get_collections(dataset_id)
    print("Get Collections")
    print(result)


def get_conformance(wfs: WFSOperations, dataset_id: str):
    result = wfs.get_conformance(dataset_id)
    print("Get Conformance")
    print(result)


def get_feature(wfs: WFSOperations, dataset_id: str):
    result = wfs.get_feature(dataset_id, "unit", "UNIT39")
    print("Get Feature")
    print(result)


def get_features(wfs: WFSOperations, dataset_id: str):
    result = wfs.get_features(dataset_id, "unit", 1, "-123,46,-120,47")
    print("Get Features")
    print(result)


def get_landing_page(wfs: WFSOperations, dataset_id: str):
    result = wfs.get_landing_page(dataset_id)
    print("Get Landing Page")
    print(result)


def main(dataset_id: str):
    wfs = create_maps_client().wfs
    get_collection(wfs, dataset_id)
    get_collections(wfs, dataset_id)
    get_collection_definition(wfs, dataset_id)
    get_conformance(wfs, dataset_id)
    get_feature(wfs, dataset_id)
    get_features(wfs, dataset_id)
    get_landing_page(wfs, dataset_id)
    delete_feature(wfs, dataset_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='WFS Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.add_argument('--dataset_id', action="store", required=True)
    main(parser.parse_args().dataset_id)
