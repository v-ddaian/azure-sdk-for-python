# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import json
import argparse

from typing import List
from azure.core.exceptions import HttpResponseError
from azure.maps.service.operations import FeatureStateOperations
from azure.maps.service.models import StatesetInfoObject, StatesetListResponse

from common.common import create_maps_client


def create_stateset(feature_state: FeatureStateOperations, dataset_id: str):
    with open("resources/featurestate_sample_create.json", "r") as file:
        style = json.loads(file.read())
        result = feature_state.create_stateset(dataset_id, style)
        print("Created stateset")
        print(result)
        return result.stateset_id


def delete_state(feature_state: FeatureStateOperations, stateset_id: str, feature_id: str, state_key_name: str):
    feature_state.delete_state(stateset_id, feature_id, state_key_name)
    print("Deleted state")


def delete_stateset(feature_state: FeatureStateOperations, stateset_id: str):
    feature_state.delete_stateset(stateset_id)
    print("Deleted stateset")


def get_states(feature_state: FeatureStateOperations, stateset_id: str, feature_id: str):
    feature_state_structure = feature_state.get_states(stateset_id, feature_id)
    print("Get states with stateset_id {} and feature_id {}".format(
        stateset_id, feature_id))
    print(feature_state_structure)


def get_stateset(feature_state: FeatureStateOperations, stateset_id: str):
    stateset = feature_state.get_stateset(stateset_id)
    print("Get states with stateset_id {}".format(stateset_id))
    print(stateset)


def list_stateset(feature_state: FeatureStateOperations):
    result = feature_state.list_stateset()
    print("List statesets:")
    for stateset in result:
        print(stateset)


def put_stateset(feature_state: FeatureStateOperations, stateset_id: str):
    with open("resources/featurestate_sample_put", "r") as file:
        style = json.loads(file.read())
        result = feature_state.put_stateset(stateset_id, style)
        print("Updated stateset")
        print(result)


def update_states(feature_state: FeatureStateOperations, stateset_id: str):
    with open("resources/featurestate_sample_update_states.json", "r") as file:
        states = json.loads(file.read())
        result = feature_state.update_states(stateset_id, states)
        print("Updated stateset")
        print(result)


def main(dataset_id: str):
    feature_state = create_maps_client().feature_state
    stateset_id = create_stateset(feature_state, dataset_id)
    feature_id = "SPC4709"
    state_key_names = "keyName1"
    try:
        list_stateset(feature_state)
        get_stateset(feature_state, stateset_id)
        get_states(feature_state, stateset_id, feature_id)
        put_stateset(feature_state, stateset_id)
        update_states(feature_state, stateset_id)
        delete_state(feature_state, stateset_id, feature_id, state_key_names)
    except HttpResponseError as e:
        print(e)
    finally:
        delete_stateset(feature_state, stateset_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Featurestate Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.add_argument('--dataset_id', action="store", required=True)
    main(parser.parse_args().dataset_id)
