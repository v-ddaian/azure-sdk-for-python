# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse

from azure.maps.service.operations import TrafficOperations
from azure.maps.service.models import TextFormat, TrafficFlowSegmentStyle, TileFormat, TrafficIncidentDetailStyle
from common.common import create_maps_client, write_stream_to_file, write_str_to_file


def get_traffic_flow_segment(traffic: TrafficOperations):
    result = traffic.get_traffic_flow_segment(
        TextFormat.JSON, TrafficFlowSegmentStyle.ABSOLUTE, 10, "52.41072,4.84239")
    print("Get Traffic Flow Segment")
    print(result)


def get_traffic_flow_tile(traffic: TrafficOperations):
    result = traffic.get_traffic_flow_tile(
        TileFormat.PNG, TrafficFlowSegmentStyle.ABSOLUTE, 12, 2044, 1360)
    print("Get Traffic Flow Tile")
    write_stream_to_file(result, "tmp/traffic_flow_tile.png")


def get_traffic_incident_detail(traffic: TrafficOperations):
    result = traffic.get_traffic_incident_detail(
        TextFormat.JSON, TrafficIncidentDetailStyle.S3, "6841263.950712,511972.674418,6886056.049288,582676.925582", 11, "1335294634919")
    print("Get Traffic Incident Detail")
    print(result)


def get_traffic_incident_tile(traffic: TrafficOperations):
    result = traffic.get_traffic_incident_tile(
        TileFormat.PNG, TrafficIncidentDetailStyle.NIGHT, 10, 175, 408)
    print("Get Traffic Incident Tile")
    write_stream_to_file(result, "tmp/traffic_incident_tile.png")


def get_traffic_incident_viewport(traffic: TrafficOperations):
    result = traffic.get_traffic_incident_viewport(TextFormat.JSON, "-939584.4813015489,-23954526.723651607,14675583.153020501,25043442.895825107",
                                                   2, "-939584.4813018347,-23954526.723651607,14675583.153020501,25043442.8958229083", 2)
    print("Get Traffic Incident Viewport")
    print(result)


def main():
    traffic = create_maps_client().traffic
    get_traffic_flow_segment(traffic)
    get_traffic_flow_tile(traffic)
    get_traffic_incident_detail(traffic)
    get_traffic_incident_tile(traffic)
    get_traffic_incident_viewport(traffic)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Traffic Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.parse_args()
    main()
