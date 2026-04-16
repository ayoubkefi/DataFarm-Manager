from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from operators import router as operator_router
from robots import router as robot_router
from sops import router as sop_router
from stations import router as station_router
from collection_items import router as colelction_item_router


app = FastAPI(
    title="DataFarm Manager",
    description="SOP & Operator management system",
    version="0.1.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(operator_router)
app.include_router(robot_router)
app.include_router(sop_router)
app.include_router(station_router)
app.include_router(colelction_item_router)

