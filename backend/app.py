from flask import Flask, request, url_for, redirect # type: ignore
from flask_cors import CORS # type: ignore
from pymongo import MongoClient # type: ignore
from pymongo.server_api import ServerApi # type: ignore
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]
import os
from database import batters_db # pyright: ignore[reportMissingImports]

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

if __name__ == '__main__':
    app.run(debug=True)
