# These examples are ingested by the documentation system, and are
# displayed in the SDK reference documentation. When editing these
# example snippets, take into consideration how this might affect
# the readability and usability of the reference documentation.
import argparse
import os

from azure.maps.service.operations import RenderOperations, RenderV2Operations
from azure.maps.service.models import TextFormat, IncludeText, MapImageryStyle, RasterTileFormat, StaticMapLayer, MapImageStyle, MapTileSize, TilesetID, TileSize

from common.common import create_maps_client, write_stream_to_file


def get_copyright_caption(render: RenderOperations):
    result = render.get_copyright_caption(TextFormat.JSON)
    print(result)


def get_copyright_for_tile(render: RenderOperations):
    result = render.get_copyright_for_tile(TextFormat.JSON, 6, 9, 22)
    print(result)


def get_copyright_for_world(render: RenderOperations):
    result = render.get_copyright_for_world(TextFormat.JSON)
    print(result)


def get_copyright_from_bounding_box(render: RenderOperations):
    result = render.get_copyright_from_bounding_box(
        TextFormat.JSON, "52.41064,4.84228", "52.41072,4.84239", IncludeText.YES)
    print(result)



def get_map_imagery_tile(render: RenderOperations):
    result = render.get_map_imagery_tile(
        RasterTileFormat.PNG, MapImageryStyle.SATELLITE, 6, 10, 22)
    write_stream_to_file(
        result, "tmp/map_imagery_tile.png")


def get_map_state_tile_preview(render: RenderOperations, stateset_id: str):
    result = render.get_map_state_tile_preview(6, 10, 22, stateset_id)
    write_stream_to_file(result, "tmp/state_tile.json")


def get_map_static_image(render: RenderOperations):
    result = render.get_map_static_image(RasterTileFormat.PNG, StaticMapLayer.BASIC,
                                         MapImageStyle.DARK, 2, None, "1.355233,42.982261,24.980233,56.526017")
    write_stream_to_file(result, "tmp/static_image.png")


def get_map_tile(render: RenderOperations):
    result = render.get_map_tile(RasterTileFormat.PNG, StaticMapLayer.BASIC,
                                 MapImageStyle.MAIN, 6, 10, 22, MapTileSize.FIVE_HUNDRED_TWELVE)
    write_stream_to_file(result, "tmp/tile.png")


def get_map_tile_v2(render_v2: RenderV2Operations):
    result = render_v2.get_map_tile_preview(
        TilesetID.MICROSOFT_BASE, 6, 10, 22, tile_size=TileSize.FIVE_HUNDRED_TWELVE)
    write_stream_to_file(result, "tmp/tile_v2.vec")


def main(stateset_id: str):
    render = create_maps_client().render
    if not os.path.isdir("tmp"):
        os.mkdir("tmp")
    get_copyright_caption(render)
    get_copyright_for_tile(render)
    get_copyright_for_world(render)
    get_copyright_from_bounding_box(render)
    get_map_imagery_tile(render)
    if stateset_id is not None:
        get_map_state_tile_preview(render, stateset_id)
    get_map_static_image(render)
    get_map_tile(render)

    render_v2 = create_maps_client().render_v2
    get_map_tile_v2(render_v2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Render Samples Program. Set SUBSCRIPTION_KEY env variable.')
    parser.add_argument('--stateset_id', action="store", default=None)
    args_parsed = parser.parse_args()
    main(args_parsed.stateset_id)
