"""
M3: A Markov Distinction
Course: Computational Creativity
Name: Jimmy Song
Date: 15 September 2024
"""

import numpy as np
import random

STARTING_HEALTH = 100

class Battle:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.attacks = list(transition_matrix.keys())

    def get_next_attack(self, current_attack):
        """Decides which attack will be used against us, based on the current attack used
        Returns: a List containning only the next attack"""
        return random.choices(
            self.attacks,
            weights = [self.transition_matrix[current_attack][next_attack]
                    for next_attack in self.attacks])
    
    def generate_battle(self, current_attack = None, num_attacks = 5):
        """Generate a sequence of attacks
        Returns: a List of performed attacks"""
        if current_attack == None:
            current_attack = random.choice(self.attacks)
        attacks = []
        while len(attacks) < num_attacks:
            next_attack = (self.get_next_attack(current_attack))[0]
            attacks.append(next_attack)
            current_attack = next_attack
        return attacks
    
def main():
    test_battle = Battle(
        {
            "flamethrower": {"flamethrower": 0.3, "hydropump": 0.1, "splash": 0.2, "focus blast": 0.4},
            "hydropump": {"flamethrower": 0.2, "hydropump": 0.2, "splash": 0.5, "focus blast": 0.1},
            "splash": {"flamethrower": 0.2, "hydropump": 0.1, "splash": 0.4, "focus blast": 0.3},
            "focus blast": {"flamethrower": 0.4, "hydropump": 0.1, "splash": 0.3, "focus blast": 0.2}
        }
    )
    print(test_battle.generate_battle())

if __name__ == "__main__":
    main()