import json

from core.engine.models.batter import Batter
from bson import ObjectId, json_util # type: ignore
from pymongo import MongoClient # type: ignore
from pymongo.server_api import ServerApi # type: ignore
import os
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]
from core.engine.simulation.simulator import Simulator # pyright: ignore[reportMissingImports]

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'), server_api=ServerApi('1'))

db = client.BaseballSimulatorDB
batters = db.batters

def get_batters():
    batters_list = list(batters.find({}))
    for batter in batters_list:
        batter['_id'] = str(batter['_id'])
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
        "avg": float(batter_data["avg"]),
        "babip": float(batter_data["babip"])
    }
    print("batter_data:", batter_data)
    result = batters.insert_one(batter_data_adjusted_types)
    return {'id': str(result.inserted_id), 'message': 'Batter created'}

def simulate_player_season(player_id):
    batter_doc = batters.find_one({'_id': ObjectId(player_id)})
    
    batter = Batter(batter_doc)
    
    simulator = Simulator(batter)
    result = simulator.simulate_at_bats(650)

    print("Simulation result:", result)
    
    return {"name": batter_doc["name"], "stats": result}