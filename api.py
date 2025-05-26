from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import load_stop_dl_data
from routers.spatial import router as spatial_router
from routers.params import router_route as route_router, router_dir as dir_router

app = FastAPI()

# include routers before CORS
app.include_router(spatial_router, prefix="/api")
app.include_router(route_router, prefix="/api")
app.include_router(dir_router, prefix="/api")

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
    df = load_stop_dl_data()
    return df.to_dict(orient="records")