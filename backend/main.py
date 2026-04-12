from engine.models.game import Game
from engine.models.batter import Batter
from engine.models.team import Team

yankees = [
    Batter(
        {
            "name":"Trent Grisham", 
            "k_rate":0.236, 
            "bb_rate":0.141, 
            "hr_rate":34/581, 
            "avg": 0.235, 
            "slg": 0.464, 
            "babip":0.253
        }
    ),
    Batter(
        {
            "name":"Aaron Judge", 
            "k_rate":0.236, 
            "bb_rate":0.183, 
            "hr_rate":53/679, 
            "avg": 0.331, 
            "slg": 0.688, 
            "babip":0.376
        }
    ),
    Batter(
        {
            "name":"Juan Soto", 
            "k_rate":0.173, 
            "bb_rate":0.187, 
            "hr_rate":244/4803, 
            "avg": 0.277, 
            "slg": 0.507, 
            "babip":0.300
         }
    ),
    Batter(
        {
            "name":"Cody Bellinger", 
            "k_rate":0.137, 
            "bb_rate":0.087, 
            "hr_rate":29/656, 
            "avg": 0.272, 
            "slg": 0.480, 
            "babip":0.274
        }
    ),
    Batter(
        {
            "name":"Giancarlo Stanton", 
            "k_rate":0.312, 
            "bb_rate":0.083, 
            "hr_rate":27/459, 
            "avg": 0.233, 
            "slg": 0.475, 
            "babip":0.281
        }
    ),
    Batter(
        {
            "name":"Jazz Chisholm Jr.", 
            "k_rate":0.279, 
            "bb_rate":0.109, 
            "hr_rate":31/531, 
            "avg": 0.242, 
            "slg": 0.481, 
            "babip":0.282
        }
    ),
    Batter(
        {
            "name":"Ryan McMahon", 
            "k_rate":0.323, 
            "bb_rate":0.119, 
            "hr_rate":20/568, 
            "avg": 0.214, 
            "slg": 0.381, 
            "babip":0.294
        }
    ),
    Batter(
        {
            "name":"Anthony Volpe", 
            "k_rate":0.252, 
            "bb_rate":0.079, 
            "hr_rate":19/596, 
            "avg": 0.212, 
            "slg": 0.391, 
            "babip":0.252
        }
    ),
    Batter(
        {
            "name":"Austin Wells", 
            "k_rate":0.263, 
            "bb_rate":0.067, 
            "hr_rate":21/448, 
            "avg": 0.219, 
            "slg": 0.436, 
            "babip":0.245
        }
    ),
]

blue_jays = [
    Batter(
        {
            "name":"George Springer", 
            "k_rate":0.189, 
            "bb_rate":0.118, 
            "hr_rate":32/586, 
            "avg": 0.309, 
            "slg": 0.560, 
            "babip":0.340
        }
    ),
    Batter(
        {
            "name":"Nathan Lukes", 
            "k_rate":0.137, 
            "bb_rate":0.087, 
            "hr_rate":12/438, 
            "avg": 0.255, 
            "slg": 0.407, 
            "babip":0.273
        }
    ),
    Batter(
        {
            "name":"Vladimir Guerrero Jr", 
            "k_rate":0.138, 
            "bb_rate":0.119, 
            "hr_rate":23/680, 
            "avg": 0.292, 
            "slg": 0.467, 
            "babip":0.313
        }
    ),
    Batter(
        {
            "name":"Bo Bichette", 
            "k_rate":0.145, 
            "bb_rate":0.064, 
            "hr_rate":18/628, 
            "avg": 0.311, 
            "slg": 0.483, 
            "babip":0.342
        }
    ),
    Batter(
        {
            "name":"Addison Barger", 
            "k_rate":0.241, 
            "bb_rate":0.072, 
            "hr_rate":21/502, 
            "avg": 0.243, 
            "slg": 0.454, 
            "babip":0.284
        }
    ),
    Batter(
        {
            "name":"Alejandro Kirk", 
            "k_rate":0.117, 
            "bb_rate":0.095, 
            "hr_rate":15/506, 
            "avg": 0.282, 
            "slg": 0.421, 
            "babip":0.292
        }
    ),
    Batter(
        {
            "name":"Daulton Varsho", 
            "k_rate":0.284, 
            "bb_rate":0.063, 
            "hr_rate":20/271, 
            "avg": 0.238, 
            "slg": 0.548, 
            "babip":0.250
        }
    ),
    Batter(
        {
            "name":"Ernie Clement", 
            "k_rate":0.104, 
            "bb_rate":0.046, 
            "hr_rate":9/588, 
            "avg": 0.277, 
            "slg": 0.398, 
            "babip":0.296
        }
    ),
    Batter(
        {
            "name":"Andres Gimenez", 
            "k_rate":0.179, 
            "bb_rate":0.068, 
            "hr_rate":7/369, 
            "avg": 0.210, 
            "slg": 0.313, 
            "babip":0.239
        }
    ),
]


game = Game(Team({"name": "Yankees", "lineup": yankees}), Team({"name":"Blue Jays", "lineup":blue_jays}))

game.simulate_game()