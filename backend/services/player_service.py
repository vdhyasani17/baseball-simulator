# TODO: this is placeholder; write this
from database.players import insert_player

def create_player(data):
    # validation / cleaning
    data["avg"] = float(data["avg"])
    
    player_id = insert_player(data)
    return {"id": str(player_id)}