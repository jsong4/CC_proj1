"""
M3: A Markov Distinction
Course: Computational Creativity
Name: Jimmy Song
Date: 15 September 2024
"""

import numpy as np
import random

class Battle:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
def main():
    test_battle = Battle(
        {
            "flamethrower": {"flamethrower": 0.3, "hydropump": 0.1, "splash": 0.2, "focus blast": 0.4},
            "hydropump": {"flamethrower": 0.2, "hydropump": 0.2, "splash": 0.5, "focus blast": 0.1},
            "splash": {"flamethrower": 0.2, "hydropump": 0.1, "splash": 0.4, "focus blast": 0.3},
            "focus blast": {"flamethrower": 0.4, "hydropump": 0.1, "splash": 0.3, "focus blast": 0.2}
        }
    )

if __name__ == "__main__":
    main()