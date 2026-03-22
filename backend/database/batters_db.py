import bson # type: ignore
from pymongo import MongoClient # type: ignore
from pymongo.server_api import ServerApi # type: ignore
import os
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'), server_api=ServerApi('1'))

db = client.BaseballSimulatorDB
batters = db.batters

def get_batters():
    batters_list = list(batters.find({}, {'_id': False}))
    return {'batters': batters_list}

def create_batter(batter_data):
    print("Received batter data:", batter_data)
    print("k-rate type:", type(float(batter_data.get("k-rate"))))
    batter_data_adjusted_types = {
        "name": batter_data["name"],
        "position": batter_data["position"],
        "k_rate": float(batter_data["k-rate"]),
        "bb_rate": float(batter_data["bb-rate"]),
        "hr_rate": float(batter_data["hr-rate"]),
        "slg": float(batter_data["slg"]),
        "avg": float(batter_data["avg"])
    }
    print("batter_data:", batter_data)
    result = batters.insert_one(batter_data_adjusted_types)
    return {'id': str(result.inserted_id), 'message': 'Batter created'}