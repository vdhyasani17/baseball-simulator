import random

class Batter:

    def __init__(self, player):
        self.name = player["name"]
        self.k_rate = player["k_rate"]
        self.bb_rate = player["bb_rate"]
        self.hr_rate = player["hr_rate"]
        self.avg = player["avg"]
        self.slg = player["slg"]
        self.babip = player["babip"]
        self.air_rate = 0.58    # using league avg balls in air
        self.popup_rate = 0.07  # using league avg popup rate
        self.flyball_rate = self.air_rate - self.popup_rate

    '''
    hr/pa => hr/ab
    pa = ab+bb
    ab = pa-bb
    '''
    def simulate_plate_appearance(self):
        r1 = random.random()
        if r1 <= self.k_rate:
            return "K"
        elif r1 <= self.k_rate + self.bb_rate:
            return "BB"
        elif r1 <= self.k_rate + self.bb_rate + self.hr_rate:
            return "HR"
        else:   # these are balls in play (hits or outs)
            r2 = random.random()

            # convert hr-per-pa to hr-per-ab
            adj_hr_rate = self.hr_rate / ((1000 - self.bb_rate*1000)/1000)

            # Using league average numbers since triples are so rare
            p_triple = 0.002
            iso = self.slg - self.avg
            p_double = iso - (3 * adj_hr_rate) - (2 * p_triple)
            p_single = self.avg - adj_hr_rate - p_triple - p_double

            # normalize hit probabilities
            total = p_single + p_double + p_triple
            p_single /= total
            p_double /= total
            p_triple /= total
            if r2 <= self.babip:    # these are hits (not hrs)
                r3 = random.random()
                if r3 < p_single:
                    return "1B"
                elif r3 < p_single + p_double:
                    return "2B"
                else:
                    return "3B"
            else:   # these are outs (flyballs, popups, and groundballs)
                r_out = random.random()
                if r_out <= 0.493:
                    return "GBO"
                elif r_out <= 0.493 + 0.444:
                    return "FLBO"
                else:
                    return "PUO"