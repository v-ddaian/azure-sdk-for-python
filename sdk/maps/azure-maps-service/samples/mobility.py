# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse
import os

from azure.core.credentials import AzureKeyCredential
from common.common import AzureKeyInQueryCredentialPolicy

from azure.maps.mobility.models import ResponseFormat, MetroAreaDetailType, TransitItineraryDetailType, TransitLineDetailType, OriginType, MetroAreaQueryType, DestinationType, ModeType, TransitTypeFilter, TransitStopQueryType, TransitStopDetailType
from azure.maps.mobility import MobilityClient


client = MobilityClient('None', x_ms_client_id=os.environ.get("CLIENT_ID", None), authentication_policy=AzureKeyInQueryCredentialPolicy(
    AzureKeyCredential(os.environ.get("SUBSCRIPTION_KEY")), "subscription-key"))

parser = argparse.ArgumentParser(
    description='Mobility Samples Program. Set SUBSCRIPTION_KEY env variable.')
parser.parse_args()


result = client.mobility.get_metro_area_info_preview(
    ResponseFormat.JSON, "121", [MetroAreaDetailType.AGENCIES])
print("Get metro area info")
print(result)


result = client.mobility.get_metro_area_preview(
    ResponseFormat.JSON, "40.648677,-74.010535", MetroAreaQueryType.POSITION)
print("Get metro area")
print(result)


result = client.mobility.get_nearby_transit_preview(
    ResponseFormat.JSON, "40.693393,-73.988310", radius=300)
print("Get nearby transit")
print(result)


result = client.mobility.get_real_time_arrivals_preview(
    ResponseFormat.JSON, "121---19919516")
print("Get realtime arrivals")
print(result)

result = client.mobility.get_transit_route_preview(
    ResponseFormat.JSON, "41.948437, -87.655334", "41.878876, -87.635918", origin_type=OriginType.POSITION, destination_type=DestinationType.POSITION, mode_type=[ModeType.PUBLIC_TRANSIT], transit_type=[TransitTypeFilter.BUS])
print("Get transit route")
print(result)
itinerary_ids = list(
    map(lambda itinerary: itinerary.itinerary_id, result.results))

for itinerary_id in itinerary_ids:
    result = client.mobility.get_transit_itinerary_preview(
        ResponseFormat.JSON, itinerary_id, [TransitItineraryDetailType.GEOMETRY])
    print("Get transit itinerary")
    print(result)


result = client.mobility.get_transit_line_info_preview(
    ResponseFormat.JSON, "121---373227", detail_type=[TransitLineDetailType.STOPS])
print("Get transit line info")
print(result)


result = client.mobility.get_transit_stop_info_preview(
    ResponseFormat.JSON, "121---14013676", query_type=TransitStopQueryType.STOP_ID, detail_type=[TransitStopDetailType.LINES])
print("Get transit stop")
print(result)
