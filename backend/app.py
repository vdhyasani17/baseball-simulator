from flask import Flask, request, url_for, redirect # type: ignore
from flask_cors import CORS # type: ignore
from pymongo import MongoClient # type: ignore
from pymongo.server_api import ServerApi # type: ignore
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]
import os
from core.database import batters_db # pyright: ignore[reportMissingImports]

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET', 'POST'])
def index():
    return '<b>Welcome to the Baseball Simulator API! Use /batters to get a list of all batters.</b>'

@app.route('/batters', methods=['GET'])
def get_batters():
    return batters_db.get_batters()

@app.route('/create-batter', methods=['POST'])
def create_batter():
    batter_data = request.get_json()
    print("batter data:", batter_data)
    return batters_db.create_batter(batter_data)

@app.route('/simulate-season/<player_id>', methods=['GET'])
def simulate_player_season(player_id):
    # Placeholder for player season simulation logic
    return batters_db.simulate_player_season(player_id)

@app.route('/simulate-game', methods=['POST'])
def simulate_game():
    #Something
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5500)
