# TODO

from fastapi import APIRouter
import geopandas as gpd
from data import load_coordinate_data
import json

router = APIRouter()

# @router.get("/spatial")
# def get_geo():
#     df = load_coordinate_data()
#     gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(x=df["long"], y=df["lat"]))
#     geojson = gdf.__geo_interface__
#     return geojson
#     # return json.loads(gdf.to_json())

@router.get("/spatial/params")
def get_filtered_geo(route: int, dir: int): # NOTE the route will be str
    df = load_coordinate_data()
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(x=df["long"], y=df["lat"]))
    filtered = gdf[
        (gdf["route"] == route) &
        (gdf["dir"] == dir)
    ]
    return json.loads(filtered.to_json())
    # return filtered.__geo_interface__
