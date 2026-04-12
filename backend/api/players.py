# TODO: this is placeholder; write this
from flask import Blueprint, request, jsonify
from services.player_service import create_player

players_bp = Blueprint("players", __name__)

@players_bp.route("/players", methods=["POST"])
def add_player():
    data = request.json
    player = create_player(data)
    return jsonify(player)