from engine.models.batter import Batter
from engine.simulation.simulator import Simulator

# Kyle Tucker (all around player)
player1 = Batter({"name":"Kyle Tucker", "k_rate":0.158, "bb_rate":0.115, "hr_rate":147/3158, "avg": 0.273, "slg": 0.507, "babip":0.284})

# Vladimir Guerrero Jr (power)
player2 = Batter({
            "name":"Vladimir Guerrero Jr", 
            "k_rate":0.138, 
            "bb_rate":0.119, 
            "hr_rate":23/680, 
            "avg": 0.292, 
            "slg": 0.467, 
            "babip":0.313
        })

# Shohei Ohtani (power)
player3 = Batter({"name":"Shohei Ohtani", "k_rate":0.255, "bb_rate":0.125, "hr_rate":280/4329, "avg": 0.282, "slg": 0.582, "babip":0.325})

# Juan Soto (all-rounder)
player4 = Batter({"name":"Juan Soto", "k_rate":0.173, "bb_rate":0.187, "hr_rate":244/4803, "avg": 0.277, "slg": 0.507, "babip":0.300})

# Luis Arraez (contact)
player5 = Batter({"name":"Luis Arraez", "k_rate":0.061, "bb_rate":0.065, "hr_rate":36/3533, "avg": 0.317, "slg": 0.413, "babip":0.329})

# Adam Dunn (power)
player6 = Batter({"name":"Adam Dunn", "k_rate":0.286, "bb_rate":0.158, "hr_rate":462/8328, "avg": 0.237, "slg": 0.490, "babip":0.283})

sim = Simulator(player5)

sim.simulate_at_bats(650)