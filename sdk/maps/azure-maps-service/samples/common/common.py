from azure.maps.service import MapsClient
import os
import re
import time


def create_maps_client():
    return MapsClient(os.environ["SUBSCRIPTION_KEY"], base_url='https://us.atlas.microsoft.com:443')


def get_operation_location(poller, location_name):
    return poller.polling_method(
    )._initial_response.http_response.headers[location_name]

def get_operation_location_id(poller, location_name):
    operation_location = get_operation_location(poller, location_name)
    return get_uid(operation_location)

def get_uid(url):
    return re.search("[0-9A-Fa-f\-]{36}", url).group()

def wait_for_status_complete(service, operation_id: str, get_operation):
    status = get_operation(service, operation_id).status
    while status != "Succeeded":
        if status == 'Failed':
            print(result.error)
            for error_detail in result.error.details[0].details:
                print(error_detail)
            return None
        time.sleep(15)
        result = get_operation(service, operation_id)
        status = result.status
        if status == "Succeeded":
            return get_uid(result.resource_location)


def write_stream_to_file(stream, filename: str):
    with open(filename, "wb") as file:
        bytes = bytearray()
        for line in stream:
            bytes.extend(line)
        file.write(bytes)
    # open file
    os.system('start {}'.format(filename))

def write_str_to_file(str, filename: str):
    with open(filename, "w") as file:
        file.write(str)
    # open file
    os.system('start {}'.format(filename))