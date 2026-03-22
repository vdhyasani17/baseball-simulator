from enum import Enum
import random

from models.batter import Batter
from models.team import Team

class Base(Enum):
    THIRD = 0
    SECOND = 1
    FIRST = 2

class Half(Enum):
    TOP = 0
    BOTTOM = 1

class Game:

    def __init__(self, road_team, home_team):
        self.road_team_name = road_team.name
        self.home_team_name = home_team.name

        self.teams = [road_team.lineup, home_team.lineup]
        self.max_innings = 9

        self.inning = 1
        self.half = False
        self.outs = 0

        self.current_batter = [0, 0]

        self.bases = [False, False, False]

        self.runs = [0, 0]
        self.hits = [0, 0]

        self.runs_by_inning = []
        self.runs_by_inning = []


    def simulate_walk(self):
        runner_on_base = self.bases[Base.FIRST.value]
        self.bases[Base.FIRST.value] = True

        if not runner_on_base:  # check if runner on first
            return
        runner_on_base = self.bases[Base.SECOND.value]
        self.bases[Base.SECOND.value] = True

        if not runner_on_base:  # check if runner on second
            return
        runner_on_base = self.bases[Base.THIRD.value]
        self.bases[Base.THIRD.value] = True

        if not runner_on_base:  # check if runner on third
            return

        # if here, runner scores
        self.runs[self.half] += 1

    
    def simulate_single(self):

        # on single, runner on third scores 100% of time
        runner_on_third = self.bases[Base.THIRD.value]
        if runner_on_third:
            self.bases[Base.THIRD.value] = False
            self.runs[self.half] += 1

        # on single, runner on second scores 47% of time
        runner_on_second = self.bases[Base.SECOND.value]
        if runner_on_second:
            self.bases[Base.SECOND.value] = False
            self.bases[Base.THIRD.value] = True
            p_scores = random.random()
            if p_scores < 0.47:
                self.bases[Base.THIRD.value] = False
                self.runs[self.half] += 1
        
        # on single, runner on first advances to third 50% of time if not already runner on third
        runner_on_first = self.bases[Base.FIRST.value]
        if runner_on_first:
            self.bases[Base.FIRST.value] = False
            self.bases[Base.SECOND.value] = True
            p_third = random.random()
            if p_third < 0.5 and not self.bases[Base.THIRD.value]:
                self.bases[Base.SECOND.value] = False
                self.bases[Base.THIRD.value] = True

        self.bases[Base.FIRST.value] = True
        
        # increment hit total
        self.hits[self.half] += 1


    def simulate_double(self):

        # on double, runner on third scores 100% of time
        runner_on_third = self.bases[Base.THIRD.value]
        if runner_on_third:
            self.bases[Base.THIRD.value] = False
            self.runs[self.half] += 1

        # on double, runner on second scores 100% of time
        runner_on_second = self.bases[Base.SECOND.value]
        if runner_on_second:
            self.bases[Base.SECOND.value] = False
            self.runs[self.half] += 1
        
        # on double, runner on first advances to third 80% of time
        runner_on_first = self.bases[Base.FIRST.value]
        if runner_on_first:
            self.bases[Base.FIRST.value] = False
            self.bases[Base.THIRD.value] = True
            p_third = random.random()
            if p_third < 0.8:
                self.bases[Base.THIRD.value] = False
                self.runs[self.half] += 1
        

        # lastly, put runner on first on single
        self.bases[Base.SECOND.value] = True

        # increment hit total
        self.hits[self.half] += 1


    def simulate_triple(self):

        # on triple, runner on third scores 100% of time
        runner_on_third = self.bases[Base.THIRD.value]
        if runner_on_third:
            self.bases[Base.THIRD.value] = False
            self.runs[self.half] += 1

        # on triple, runner on second scores 100% of time
        runner_on_second = self.bases[Base.SECOND.value]
        if runner_on_second:
            self.bases[Base.SECOND.value] = False
            self.runs[self.half] += 1
        
        # on triple, runner on first scores 100% of time
        runner_on_first = self.bases[Base.FIRST.value]
        if runner_on_first:
            self.bases[Base.FIRST.value] = False
            self.runs[self.half] += 1
        

        # lastly, put runner on first on single
        self.bases[Base.THIRD.value] = True

        # increment hit total
        self.hits[self.half] += 1

    
    def simulate_hr(self):

        # on hr, runner on third scores 100% of time
        runner_on_third = self.bases[Base.THIRD.value]
        if runner_on_third:
            self.bases[Base.THIRD.value] = False
            self.runs[self.half] += 1

        # on hr, runner on second scores 100% of time
        runner_on_second = self.bases[Base.SECOND.value]
        if runner_on_second:
            self.bases[Base.SECOND.value] = False
            self.runs[self.half] += 1
        
        # on hr, runner on first scores 100% of time
        runner_on_first = self.bases[Base.FIRST.value]
        if runner_on_first:
            self.bases[Base.FIRST.value] = False
            self.runs[self.half] += 1
        

        # lastly, score last runner (the batter who hit hr)
        self.runs[self.half] += 1

        # increment hit total
        self.hits[self.half] += 1


    def simulate_pa(self):
        pass
    
    
    def simulate_half_inning(self, verbose_outs=False):
        side = self.half

        # scratch code: don't run bottom 9 if ahead
        if self.inning >= 9 and self.half == Half.BOTTOM.value and self.runs[1] > self.runs[0]:
            return

        if self.half == Half.TOP.value:
            self.runs_by_inning.append([0, 0])
            print(f"TOP {self.inning}")
        else:
            print(f"BOTTOM {self.inning}")
        runs_at_start = self.runs[self.half]
        while self.outs < 3:
            out_outcomes = ['K', 'GBO','FLBO', 'PUO']
            res = self.teams[side][self.current_batter[side] % 9].simulate_plate_appearance()
            if res in out_outcomes:
                self.outs += 1
                if verbose_outs:
                    if res == 'K':
                        print(f"{self.teams[side][self.current_batter[side] % 9].name} STRIKES OUT", end=" ")
                    elif res == 'GBO':
                        print(f"{self.teams[side][self.current_batter[side] % 9].name} GROUNDS OUT", end=" ")
                    elif res == 'FLBO':
                        print(f"{self.teams[side][self.current_batter[side] % 9].name} FLIES OUT", end=" ")
                    elif res == 'K':
                        print(f"{self.teams[side][self.current_batter[side] % 9].name} POPS OUT", end=" ")
                    print(f"({self.outs} OUT)")
                else:
                    print(f"{self.outs} OUT")
            elif res == '1B':
                self.simulate_single()
                print(f"{self.teams[side][self.current_batter[side] % 9].name} SINGLES {self.runs}")
            elif res == '2B':
                self.simulate_double()
                print(f"{self.teams[side][self.current_batter[side] % 9].name} DOUBLES {self.runs}")
            elif res == '3B':
                self.simulate_triple()
                print(f"{self.teams[side][self.current_batter[side] % 9].name} TRIPLES {self.runs}")
            elif res == 'HR':
                self.simulate_hr()
                print(f"{self.teams[side][self.current_batter[side] % 9].name} HOMERS {self.runs}")
            elif res == 'BB':
                self.simulate_walk()
                print(f"{self.teams[side][self.current_batter[side] % 9].name} WALKS {self.runs}")
            self.current_batter[side] += 1

            # if walkoff
            if self.runs[1] > self.runs[0] and self.inning >= 9 and self.half == Half.BOTTOM.value:
                break
        self.runs_by_inning[self.inning-1][self.half] = self.runs[self.half] - runs_at_start
        print() # add empty line (for formatting in terminal)
        self.bases = [False, False, False]
        self.outs = 0
        self.half ^= 1
        self.inning += 1 if self.half == 0 else 0


    def simulate_game(self):
        # first 8 1/2 innings, play normally
        for _ in range(self.max_innings * 2 - 1):
            self.simulate_half_inning()

        # if home team winning after 8 1/2 innings, game ends
        # else, play bottom 9
        if self.runs[1] > self.runs[0]:
            return
        self.simulate_half_inning()

        # as long as game is tied, play two half innings
        while self.runs[0] == self.runs[1]:
            self.simulate_half_inning()
            self.simulate_half_inning()

    
    def print_scorecard(self):
        width_number = 4  # width per inning column
        name_width = max(len(self.road_team_name), len(self.home_team_name)) + 2

        # --- Header ---
        print(" " * name_width, end="")
        for i in range(len(self.runs_by_inning)):
            print(f"{i+1:>{width_number}}", end="")
        print(f"  | {'R':>{width_number-1}} {'H':>{width_number}}")

        # --- Away team row ---
        print(f"{self.road_team_name:<{name_width}}", end="")
        for inning in self.runs_by_inning:
            print(f"{inning[0]:>{width_number}}", end="")
        print(f"  |{self.runs[0]:>{width_number}} {self.hits[0]:>{width_number}}")

        # --- Home team row ---
        print(f"{self.home_team_name:<{name_width}}", end="")
        for inning in self.runs_by_inning:
            print(f"{inning[1]:>{width_number}}", end="")
        print(f"  |{self.runs[1]:>{width_number}} {self.hits[1]:>{width_number}}\n")


    def reset_game(self):
        self.inning = 1
        self.half = False
        self.outs = 0

        self.current_batter = [0, 0]

        self.bases = [False, False, False]

        self.runs = [0, 0]
        self.hits = [0, 0]

        self.runs_by_inning = []
        self.runs_by_inning = []
        
        
    


