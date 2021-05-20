# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse

from azure.maps.service.operations import AliasOperations
from azure.core.exceptions import HttpResponseError
from typing import List
from common.common import create_maps_client


def create(alias: AliasOperations):
    alias_create_response = alias.create()
    print("Created alias with:")
    print(alias_create_response)
    return alias_create_response.alias_id


def assign(alias: AliasOperations, alias_id: str, creator_data_item_id: str):
    alias_list_item = alias.assign(alias_id, creator_data_item_id)
    print("Assigned resource with creator_data_item_id {} to alias with alias_id: {}".format(
        creator_data_item_id, alias_id))
    print(alias_list_item)


def list(alias: AliasOperations):
    aliases = alias.list()
    print("View all previously created aliases:")
    for alias_list_item in aliases:
        print(alias_list_item)


def delete(alias: AliasOperations, alias_id: str):
    alias.delete(alias_id)
    print("Deleted alias with aliasId: {}".format(alias_id))


def get_details(alias: AliasOperations, alias_id: str):
    alias_list_item = alias.get_details(alias_id)
    print("Got details of alias:")
    print(alias_list_item)


def main(creator_data_item_id: str):
    alias = create_maps_client().alias
    alias_id = create(alias)
    try:
        if creator_data_item_id != None:
            assign(alias, alias_id, creator_data_item_id=creator_data_item_id)
        get_details(alias, alias_id)
        list(alias)
    except HttpResponseError as e:
        print(e)
    finally:
        delete(alias, alias_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Alias Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.add_argument('--creator_data_item_id', action="store", default=None)
    main(parser.parse_args().creator_data_item_id)
