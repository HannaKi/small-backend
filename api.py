from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import geopandas as gpd
from data import load_all_data, load_coordinate_data
import json


app = FastAPI()

# Add CORS when running frontend on a different port
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in prod!
    allow_methods=["*"],
    allow_headers=["*"],
)


# routers to serve data
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI root!"}


@app.get("/data")
def get_data():
    df = load_all_data()
    return df.to_dict(orient="records")


@app.get("/spatial")
def get_geo():
    df = load_coordinate_data()
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(x=df["long"], y=df["lat"]))
    geojson = gdf.__geo_interface__
    return geojson

@app.get("/spatial/params")
def get_filtered_geo(route: int, dir: int):
    df = load_coordinate_data()
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(x=df["long"], y=df["lat"]))
    filtered = gdf[
        (gdf["route"] == route) &
        (gdf["dir"] == dir)
    ]
    return json.loads(filtered.to_json())
