# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse
from typing import List
import sys
import json
import zipfile

from azure.maps.service.operations import DataOperations
from azure.maps.service.models import UploadDataFormat, MapDataListResponse, MapDataDetailInfo
from azure.core.exceptions import HttpResponseError
from common.common import create_maps_client, get_operation_location_id, wait_for_status_complete

import gzip
from io import StringIO, BytesIO


def upload(data: DataOperations):
    with open("resources/data_sample_upload.json", "r") as file:
        poller = data.begin_upload_preview(UploadDataFormat.GEOJSON,
                                           json.loads(file.read()), "Upload Description", polling=True)
        operation_id = get_operation_location_id(poller, "operation-location")
        print("Uploaded file with udid {}".format(operation_id))
        return operation_id


def upload_zip(data: DataOperations):
    with open("resources/Sample - Contoso Drawing Package.zip", "rb") as file:
        poller = data.begin_upload_preview(UploadDataFormat.DWGZIPPACKAGE,
                                           file.read(), "Upload Description", polling=True, content_type="application/octet-stream")
        operation_id = get_operation_location_id(poller, "operation-location")
        print("Uploaded file with udid {}".format(operation_id))
        return operation_id


def update(data: DataOperations, udid: str):
    with open("resources/data_sample_update.json", "r") as file:
        poller = data.begin_update_preview(udid, json.loads(file.read()),
                                           "Update Description")
        operation_id = get_operation_location_id(poller, "operation-location")
        print("Updated file with udid {}".format(udid))
        return operation_id


def delete(data: DataOperations, udid: str):
    data.delete_preview(udid)
    print("Deleted file with udid {}".format(udid))


def download(data: DataOperations, udid: str):
    fileData = data.download_preview(udid)
    bytes = bytearray()
    for line in fileData:
        bytes.extend(line)
    print("Downloaded file with udid {}".format(udid))
    print(bytes)


def list(data: DataOperations):
    result: MapDataListResponse = data.list_preview()
    files: List[MapDataDetailInfo] = result.map_data_list
    print("View all uploaded files:")
    for map_data_detail in files:
        print(map_data_detail)


def get_operation(data: DataOperations, operation_id: str):
    result = data.get_operation_preview(operation_id)
    print("Get file with operation_id {}".format(operation_id))
    print(result)
    return result


def main(do_delete: bool):
    data = create_maps_client().data
    operation_id = upload(data)
    udid = wait_for_status_complete(data, operation_id, get_operation)
    if udid is None:
        print("File upload faled")
        return
    #operation_id_zip = upload_zip(data)
    #udid_zip = wait_for_status_complete(data, operation_id_zip, get_operation)
    #if udid_zip is None:
    #    print("Zip file upload faled")
    #    return
    try:
        list(data)
        download(data, udid)
        operation_id = update(data, udid)
        if not wait_for_status_complete(data, operation_id, get_operation):
            print("File update failed")
            return
    except HttpResponseError as e:
        print(e)
    finally:
        if do_delete:
            delete(data, udid)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Data Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.add_argument('--dont_delete',
                        action="store_true", default=False)
    main(not parser.parse_args().dont_delete)
