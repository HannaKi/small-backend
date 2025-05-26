# TODO

from fastapi import APIRouter
from data import load_route_data, load_dir_data

router_route = APIRouter()
router_dir = APIRouter()

@router_route.get("/params/route")
def get_routes():
    df = load_route_data()
    return df.to_dict(orient="records")

@router_dir.get("/params/dir")
def get_dirs():
    df = load_dir_data()
    return df.to_dict(orient="records")