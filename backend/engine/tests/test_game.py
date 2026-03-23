from engine.models.batter import Batter
from engine.models.team import Team
from engine.models.game import Game
from engine.data.batters import luis_arraez, juan_soto, aaron_judge, adam_dunn, vladimir_guerrero, god

road_lineup = [
    Batter(
        {
            "name":"Joe1", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe2", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe3", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe4", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe5", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe6", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe7", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ),
    Batter(
        {
            "name":"Joe8", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe9", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ),  
]

home_lineup = [
    Batter(
        {
            "name":"Joe1", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe2", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe3", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe4", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe5", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe6", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe7", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ),
    Batter(
        {
            "name":"Joe8", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ), 
    Batter(
        {
            "name":"Joe9", 
            "k_rate":0.225, 
            "bb_rate":0.086, 
            "hr_rate":0.033, 
            "avg": 0.248, 
            "slg": 0.414, 
            "babip":0.300
        }
    ),  
]

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
    luis_arraez,
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

aaron_judge = [
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
            "name":"Aaron Judge", 
            "k_rate":0.236, 
            "bb_rate":0.183, 
            "hr_rate":53/679, 
            "avg": 0.331, 
            "slg": 0.688, 
            "babip":0.376
        }
    ),
]

juan_soto = Team({"name": "Sotos", 
                  "lineup": [
    Batter({"name":"Juan Soto", "k_rate":0.173, "bb_rate":0.187, "hr_rate":244/4803, "avg": 0.277, "slg": 0.507, "babip":0.300}),
    Batter({"name":"Juan Soto", "k_rate":0.173, "bb_rate":0.187, "hr_rate":244/4803, "avg": 0.277, "slg": 0.507, "babip":0.300}),
    Batter({"name":"Juan Soto", "k_rate":0.173, "bb_rate":0.187, "hr_rate":244/4803, "avg": 0.277, "slg": 0.507, "babip":0.300}),
    Batter({"name":"Juan Soto", "k_rate":0.173, "bb_rate":0.187, "hr_rate":244/4803, "avg": 0.277, "slg": 0.507, "babip":0.300}),
    Batter({"name":"Juan Soto", "k_rate":0.173, "bb_rate":0.187, "hr_rate":244/4803, "avg": 0.277, "slg": 0.507, "babip":0.300}),
    Batter({"name":"Juan Soto", "k_rate":0.173, "bb_rate":0.187, "hr_rate":244/4803, "avg": 0.277, "slg": 0.507, "babip":0.300}),
    Batter({"name":"Juan Soto", "k_rate":0.173, "bb_rate":0.187, "hr_rate":244/4803, "avg": 0.277, "slg": 0.507, "babip":0.300}),
    Batter({"name":"Juan Soto", "k_rate":0.173, "bb_rate":0.187, "hr_rate":244/4803, "avg": 0.277, "slg": 0.507, "babip":0.300}),
    Batter({"name":"Juan Soto", "k_rate":0.173, "bb_rate":0.187, "hr_rate":244/4803, "avg": 0.277, "slg": 0.507, "babip":0.300}),
]})

luis_arraez_lineup = Team(
    {
    "name": "Arraez", 
    "lineup": [
        luis_arraez,
        luis_arraez,
        luis_arraez,
        luis_arraez,
        luis_arraez,
        luis_arraez,
        luis_arraez,
        luis_arraez,
        luis_arraez,
    ]
    })

adam_dunn_lineup = Team({
    "name": "Dunns",
    "lineup": [
        adam_dunn,
        adam_dunn,
        adam_dunn,
        adam_dunn,
        adam_dunn,
        adam_dunn,
        adam_dunn,
        adam_dunn,
        adam_dunn
    ]
})

arraez_dunn = Team({
    "name": "Arraez Dunns",
    "lineup": [
        luis_arraez,
        adam_dunn,
        luis_arraez,
        adam_dunn,
        luis_arraez,
        adam_dunn,
        luis_arraez,
        adam_dunn,
        luis_arraez,
    ]
})

dunn_arraez = Team({
    "name": "Dunn Arraez",
    "lineup": [
        adam_dunn,
        luis_arraez,
        adam_dunn,
        luis_arraez,
        adam_dunn,
        luis_arraez,
        adam_dunn,
        luis_arraez,
        adam_dunn,
    ]
})

vlad_arraez = Team({
    "name": "Vlad Arraez",
    "lineup": [
        vladimir_guerrero,
        luis_arraez,
        vladimir_guerrero,
        luis_arraez,
        vladimir_guerrero,
        luis_arraez,
        vladimir_guerrero,
        luis_arraez,
        vladimir_guerrero,
    ]
})

arraez_with_god = Team({
    "name": "Arraez with God",
    "lineup": [
        god,
        god,
        god,
        god,
        god,
        god,
        god,
        god,
        luis_arraez,
    ]
})

brewers = [
    Batter(
        {
            "name":"Jackson Chourio", 
            "k_rate":0.205, 
            "bb_rate":0.051, 
            "hr_rate":21/589, 
            "avg": 0.270, 
            "slg": 0.463, 
            "babip":0.308
        }
    ),
    Batter(
        {
            "name":"Brice Turang", 
            "k_rate":0.228, 
            "bb_rate":0.100, 
            "hr_rate":18/659, 
            "avg": 0.288, 
            "slg": 0.435, 
            "babip":0.356
        }
    ),
    Batter(
        {
            "name":"William Contreras", 
            "k_rate":0.182, 
            "bb_rate":0.127, 
            "hr_rate":17/659, 
            "avg": 0.260, 
            "slg": 0.399, 
            "babip":0.299
        }
    ),
    Batter(
        {
            "name":"Christian Yelich", 
            "k_rate":0.259, 
            "bb_rate":0.099, 
            "hr_rate":29/644, 
            "avg": 0.264, 
            "slg": 0.452, 
            "babip":0.323
        }
    ),
    Batter(
        {
            "name":"Andrew Vaughn", 
            "k_rate":0.179, 
            "bb_rate":0.073, 
            "hr_rate":14/447, 
            "avg": 0.254, 
            "slg": 0.411, 
            "babip":0.280
        }
    ),
    Batter(
        {
            "name":"Jake Bauers", 
            "k_rate":0.271, 
            "bb_rate":0.147, 
            "hr_rate":7/218, 
            "avg": 0.235, 
            "slg": 0.399, 
            "babip":0.305
        }
    ),
    Batter(
        {
            "name":"Sal Frelick", 
            "k_rate":0.135, 
            "bb_rate":0.079, 
            "hr_rate":12/594, 
            "avg": 0.288, 
            "slg": 0.405, 
            "babip":0.317
        }
    ),
    Batter(
        {
            "name":"Caleb Durbin", 
            "k_rate":0.099, 
            "bb_rate":0.059, 
            "hr_rate":11/506, 
            "avg": 0.256, 
            "slg": 0.287, 
            "babip":0.265
        }
    ),
    Batter(
        {
            "name":"Blake Perkins", 
            "k_rate":0.275, 
            "bb_rate":0.088, 
            "hr_rate":3/171, 
            "avg": 0.226, 
            "slg": 0.348, 
            "babip":0.305
        }
    ),
]

game = Game(Team({"name": "Yankees", "lineup": yankees}), Team({"name":"Blue Jays", "lineup":blue_jays}))

# test walk
def test_walk():
    for _ in range(10):
        game.simulate_walk()
        print(f"Bases: {game.bases}, {game.runs}")
    print(f"Score: {game.runs}")

# test half inning
def test_half_inning():
    i = 0
    while i < 18 or game.runs[0] == game.runs[1]:
        game.simulate_half_inning()
        print(f"{game.runs}\n")
        game.simulate_half_inning()
        print(f"{game.runs}\n")
        i += 2
    print(f"Score: {game.runs}")
    print(f"Hits: {game.hits}")

# test game function
def test_game():
    game.simulate_game()
    print(f"Score: {game.runs}")
    print(f"Hits: {game.hits}")
    print()
    game.print_scorecard()

def play_games(n):
    wins = [0, 0]
    for _ in range(n):
        game.simulate_game()
        wins[game.runs[1] > game.runs[0]] += 1
        game.reset_game()
    print(f"Wins: {wins}")

test_game()