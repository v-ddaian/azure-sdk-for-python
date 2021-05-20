# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse
from typing import List

from azure.maps.service.models import ConversionListDetailInfo
from azure.maps.service.operations import ConversionOperations
from azure.core.exceptions import HttpResponseError
from common.common import create_maps_client, get_operation_location_id, wait_for_status_complete


def convert(conversion: ConversionOperations, udid: str):
    poller = conversion.begin_convert(udid, "facility-2.0")
    operation_id = get_operation_location_id(poller, "operation-location")
    print("Created conversion with operation_id {}".format(operation_id))
    return operation_id


def get_operation(conversion: ConversionOperations, operation_id: str):
    conversionInfo = conversion.get_operation(operation_id)
    print("Get conversion operation with operation_id {}".format(operation_id))
    print(conversionInfo)
    return conversionInfo


def get(conversion: ConversionOperations, conversion_id: str):
    conversionInfo = conversion.get(conversion_id)
    print(conversionInfo)


def delete(conversion: ConversionOperations, conversion_id: str):
    conversion.delete(conversion_id)
    print("Deleted conversion with conversion_id {}".format(conversion_id))


def list(conversion: ConversionOperations):
    conversions = conversion.list()
    print("Viewing all conversions:")
    for conversionInfo in conversions:
        print(conversionInfo)


def main(udid: str, do_delete: bool):
    conversion = create_maps_client().conversion
    operation_id = convert(conversion, udid)
    conversion_id = wait_for_status_complete(conversion, operation_id, get_operation)
    if not conversion_id:
        print("Conversion failed")
        return
    try:
        get(conversion, conversion_id)
        list(conversion)
    except HttpResponseError as e:
        print(e)
    finally:
        if do_delete:
            delete(conversion, conversion_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Conversion Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.add_argument('--udid', action="store", required=True)
    parser.add_argument('--dont_delete',
                        action="store_true", default=False)
    main(parser.parse_args().udid, not parser.parse_args().dont_delete)
