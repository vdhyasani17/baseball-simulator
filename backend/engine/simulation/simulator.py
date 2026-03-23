from engine.models.batter import Batter

class Simulator:
    
    def __init__(self, batter):
        self.batter = batter

    def print_stats(self, outcomes):
        hit_outcomes = ['1B', '2B', '3B', 'HR']
        hits, total_abs = 0, 0
        on_base, pa = 0, 0
        total_bases = 0
        for key, value in outcomes.items():
            if key == 'BB':
                on_base += value
            else:
                if key in hit_outcomes:
                    multiplier = 1
                    if key == '2B':
                        multiplier = 2
                    elif key == '3B':
                        multiplier = 3
                    elif key == 'HR':
                        multiplier = 4
                    total_bases += (multiplier * value)
                    hits += value
                    on_base += value
                total_abs += value
            pa += value

        avg = hits/total_abs
        obp = on_base/pa
        slg = total_bases/total_abs
        print(f"{outcomes['K']} K")
        print(f"{outcomes['BB']} BB")
        print(f"{outcomes['1B']} 1B")
        print(f"{outcomes['2B']} 2B")
        print(f"{outcomes['3B']} 3B")
        print(f"{outcomes['HR']} HR")
        print(f"{hits}-{total_abs}")
        print(f"{avg:.3f} / {obp:.3f} / {slg:.3f}")

    def get_stats(self, outcomes):
        hit_outcomes = ['1B', '2B', '3B', 'HR']
        hits, total_abs = 0, 0
        on_base, pa = 0, 0
        total_bases = 0
        for key, value in outcomes.items():
            if key == 'BB':
                on_base += value
            else:
                if key in hit_outcomes:
                    multiplier = 1
                    if key == '2B':
                        multiplier = 2
                    elif key == '3B':
                        multiplier = 3
                    elif key == 'HR':
                        multiplier = 4
                    total_bases += (multiplier * value)
                    hits += value
                    on_base += value
                total_abs += value
            pa += value

        avg = hits/total_abs
        obp = on_base/pa
        slg = total_bases/total_abs

        return {
            "K": outcomes['K'],
            "BB": outcomes['BB'],
            "1B": outcomes['1B'],
            "2B": outcomes['2B'],
            "3B": outcomes['3B'],
            "HR": outcomes['HR'],
            "FOR": f"{hits}-{total_abs}",
            "AVG": f"{avg:.3f}",
            "OBP": f"{obp:.3f}",
            "SLG": f"{slg:.3f}"
        }

    def simulate_at_bats(self, num_pa):
        outcomes = {'K': 0, 'BB': 0, 'HR': 0, '1B': 0, '2B': 0, '3B': 0, 'GBO': 0, 'FLBO': 0, 'PUO': 0}
        # print(self.batter.name + "\n")
        for i in range(num_pa):
            outcome = self.batter.simulate_plate_appearance()
            outcomes[outcome] += 1
        
        # self.print_stats(outcomes)
        return self.get_stats(outcomes)
