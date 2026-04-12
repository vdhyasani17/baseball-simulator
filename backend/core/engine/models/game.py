from enum import Enum
import random

from engine.models.batter import Batter
from engine.models.team import Team

import time

class Base(Enum):
    THIRD = 0
    SECOND = 1
    FIRST = 2

class Half(Enum):
    TOP = 0
    BOTTOM = 1

class GameState:
    def __init__(self):
        self.inning = 1
        self.half_inning = False
        self.outs = 0

        self.current_batter = [0, 0]

        self.bases = [False, False, False]

class Game:

    def __init__(self, road_team, home_team):
        self.game_state = GameState()

        self.road_team_name = road_team.name
        self.home_team_name = home_team.name

        self.teams = [road_team.lineup, home_team.lineup]
        self.max_innings = 9

        self.runs = [0, 0]
        self.hits = [0, 0]

        self.runs_by_inning = []

        self.outcome_map = {
            '1B': self.simulate_single,
            '2B': self.simulate_double,
            '3B': self.simulate_triple,
            'HR': self.simulate_hr,
            'BB': self.simulate_walk
        }


    def simulate_walk(self):
        gs = self.game_state

        runner_on_base = gs.bases[Base.FIRST.value]
        gs.bases[Base.FIRST.value] = True

        print(f"{self.teams[gs.half_inning][gs.current_batter[gs.half_inning] % 9].name} WALKS", end=" ")

        if not runner_on_base:  # check if runner on first
            print(f"{self.runs} {gs.bases}")
            return
        runner_on_base = gs.bases[Base.SECOND.value]
        gs.bases[Base.SECOND.value] = True

        if not runner_on_base:  # check if runner on second
            print(f"{self.runs} {gs.bases}")
            return
        runner_on_base = gs.bases[Base.THIRD.value]
        gs.bases[Base.THIRD.value] = True

        if not runner_on_base:  # check if runner on third
            print(f"{self.runs} {gs.bases}")
            return

        # if here, runner scores
        self.runs[gs.half_inning] += 1

        # print outcome at the end
        print(f"{self.runs} {gs.bases}")

    
    def simulate_single(self):
        gs = self.game_state

        # on single, runner on third scores 100% of time
        runner_on_third = gs.bases[Base.THIRD.value]
        if runner_on_third:
            gs.bases[Base.THIRD.value] = False
            self.runs[gs.half_inning] += 1

        # on single, runner on second scores 47% of time
        runner_on_second = gs.bases[Base.SECOND.value]
        if runner_on_second:
            gs.bases[Base.SECOND.value] = False
            gs.bases[Base.THIRD.value] = True
            p_scores = random.random()
            if p_scores < 0.47:
                gs.bases[Base.THIRD.value] = False
                self.runs[gs.half_inning] += 1
        
        # on single, runner on first advances to third 50% of time if not already runner on third
        runner_on_first = gs.bases[Base.FIRST.value]
        if runner_on_first:
            gs.bases[Base.FIRST.value] = False
            gs.bases[Base.SECOND.value] = True
            p_third = random.random()
            if p_third < 0.5 and not gs.bases[Base.THIRD.value]:
                gs.bases[Base.SECOND.value] = False
                gs.bases[Base.THIRD.value] = True

        gs.bases[Base.FIRST.value] = True
        
        # increment hit total
        self.hits[gs.half_inning] += 1

        # print outcome at the end
        print(f"{self.teams[gs.half_inning][gs.current_batter[gs.half_inning] % 9].name} SINGLES {self.runs} {gs.bases}")


    def simulate_double(self):
        gs = self.game_state

        # on double, runner on third scores 100% of time
        runner_on_third = gs.bases[Base.THIRD.value]
        if runner_on_third:
            gs.bases[Base.THIRD.value] = False
            self.runs[gs.half_inning] += 1

        # on double, runner on second scores 100% of time
        runner_on_second = gs.bases[Base.SECOND.value]
        if runner_on_second:
            gs.bases[Base.SECOND.value] = False
            self.runs[gs.half_inning] += 1
        
        # on double, runner on first advances to third 80% of time
        runner_on_first = gs.bases[Base.FIRST.value]
        if runner_on_first:
            gs.bases[Base.FIRST.value] = False
            gs.bases[Base.THIRD.value] = True
            p_third = random.random()
            if p_third < 0.8:
                gs.bases[Base.THIRD.value] = False
                self.runs[gs.half_inning] += 1
        

        # lastly, put runner on first on single
        gs.bases[Base.SECOND.value] = True

        # increment hit total
        self.hits[gs.half_inning] += 1

        # print outcome at the end
        print(f"{self.teams[gs.half_inning][gs.current_batter[gs.half_inning] % 9].name} DOUBLES {self.runs} {gs.bases}")


    def simulate_triple(self):
        gs = self.game_state

        # on triple, runner on third scores 100% of time
        runner_on_third = gs.bases[Base.THIRD.value]
        if runner_on_third:
            gs.bases[Base.THIRD.value] = False
            self.runs[gs.half_inning] += 1

        # on triple, runner on second scores 100% of time
        runner_on_second = gs.bases[Base.SECOND.value]
        if runner_on_second:
            gs.bases[Base.SECOND.value] = False
            self.runs[gs.half_inning] += 1
        
        # on triple, runner on first scores 100% of time
        runner_on_first = gs.bases[Base.FIRST.value]
        if runner_on_first:
            gs.bases[Base.FIRST.value] = False
            self.runs[gs.half_inning] += 1
        

        # lastly, put runner on first on single
        gs.bases[Base.THIRD.value] = True

        # increment hit total
        self.hits[gs.half_inning] += 1

        # print outcome at the end
        print(f"{self.teams[gs.half_inning][gs.current_batter[gs.half_inning] % 9].name} TRIPLES {self.runs} {gs.bases}")

    
    def simulate_hr(self):
        gs = self.game_state

        # on hr, runner on third scores 100% of time
        runner_on_third = gs.bases[Base.THIRD.value]
        if runner_on_third:
            gs.bases[Base.THIRD.value] = False
            self.runs[gs.half_inning] += 1

        # on hr, runner on second scores 100% of time
        runner_on_second = gs.bases[Base.SECOND.value]
        if runner_on_second:
            gs.bases[Base.SECOND.value] = False
            self.runs[gs.half_inning] += 1
        
        # on hr, runner on first scores 100% of time
        runner_on_first = gs.bases[Base.FIRST.value]
        if runner_on_first:
            gs.bases[Base.FIRST.value] = False
            self.runs[gs.half_inning] += 1
        

        # lastly, score last runner (the batter who hit hr)
        self.runs[gs.half_inning] += 1

        # increment hit total
        self.hits[gs.half_inning] += 1

        # print outcome at the end
        print(f"{self.teams[gs.half_inning][gs.current_batter[gs.half_inning] % 9].name} HOMERS {self.runs} {gs.bases}")


    def simulate_pa(self):
        pass
    
    
    def simulate_half_inning(self, verbose_outs=False):
        gs = self.game_state

        side = gs.half_inning

        # scratch code: don't run bottom 9 if ahead
        if gs.inning >= 9 and gs.half_inning == Half.BOTTOM.value and self.runs[1] > self.runs[0]:
            return

        if gs.half_inning == Half.TOP.value:
            self.runs_by_inning.append([0, 0])
            print(f"TOP {gs.inning}")
        else:
            print(f"BOTTOM {gs.inning}")
        runs_at_start = self.runs[gs.half_inning]
        while gs.outs < 3:
            out_outcomes = ['K', 'GBO','FLBO', 'PUO']
            res = self.teams[side][gs.current_batter[side] % 9].simulate_plate_appearance()
            if res in out_outcomes:
                gs.outs += 1
                if verbose_outs:
                    if res == 'K':
                        print(f"{self.teams[side][gs.current_batter[side] % 9].name} STRIKES OUT", end=" ")
                    elif res == 'GBO':
                        print(f"{self.teams[side][gs.current_batter[side] % 9].name} GROUNDS OUT", end=" ")
                    elif res == 'FLBO':
                        print(f"{self.teams[side][gs.current_batter[side] % 9].name} FLIES OUT", end=" ")
                    elif res == 'K':
                        print(f"{self.teams[side][gs.current_batter[side] % 9].name} POPS OUT", end=" ")
                    print(f"({gs.outs} OUT)")
                else:
                    print(f"{gs.outs} OUT")
            else:
                self.outcome_map[res]() # calls function specified in map
            gs.current_batter[side] += 1

            # if walkoff
            if self.runs[1] > self.runs[0] and gs.inning >= 9 and gs.half_inning == Half.BOTTOM.value:
                break
        self.runs_by_inning[gs.inning-1][gs.half_inning] = self.runs[gs.half_inning] - runs_at_start
        print() # add empty line (for formatting in terminal)
        gs.bases = [False, False, False]
        gs.outs = 0
        gs.half_inning ^= 1
        gs.inning += 1 if gs.half_inning == 0 else 0


    def simulate_game(self):
        gs = self.game_state

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
        gs = self.game_state

        width_number = 4  # width per inning column
        name_width = max(len(self.road_team_name), len(self.home_team_name)) + 2

        # --- Header ---
        print(" " * name_width, end="")
        for i in range(len(self.runs_by_inning)):
            print(f"{i+1:>{width_number}}", end="")
        print(f"  | {'R':>{width_number-1}} {'H':>{width_number}}")
        print("-" * name_width, end="")
        print("-" * (width_number * len(self.runs_by_inning)), end="")
        print("-" * 12)

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
        self.half_inning = False
        self.outs = 0

        self.current_batter = [0, 0]

        self.bases = [False, False, False]

        self.runs = [0, 0]
        self.hits = [0, 0]

        self.runs_by_inning = []
        self.runs_by_inning = []
        
        
    


