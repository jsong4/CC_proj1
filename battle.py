"""
M3: A Markov Distinction
Course: Computational Creativity
Name: Jimmy Song
Date: 15 September 2024
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from PIL import Image

STARTING_HEALTH = 100
ATTACKS = 5

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
    
    def generate_battle(self, current_attack = None, num_attacks = ATTACKS):
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
            "flamethrower": {"flamethrower": 0.3, "judgement": 0.1, "splash": 0.2, "draco meteor": 0.4},
            "judgement": {"flamethrower": 0.2, "judgement": 0.2, "splash": 0.5, "draco meteor": 0.1},
            "splash": {"flamethrower": 0.2, "judgement": 0.1, "splash": 0.4, "draco meteor": 0.3},
            "draco meteor": {"flamethrower": 0.4, "judgement": 0.1, "splash": 0.3, "draco meteor": 0.2}
        }
    )

    battle = test_battle.generate_battle()

    blissey_img = Image.open("/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/blissey.png")
    arceus_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/arceus.jpeg')
    flamethrower_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/Arceus_Flamethrower.webp')
    judgement_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/Arceus_judgement.png')
    dracometeor_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/Arceus_dracometeor.png')

    # Create a figure and axes
    fig, axes = plt.subplots(1, ATTACKS+2, figsize=(10, 5))  # 1 row, 2 columns

    # Display the first image
    axes[0].imshow(blissey_img)
    axes[0].set_title("I choose Blissey!", fontsize=6)
    axes[0].axis('off')  # Hide axes

    # Display the second image
    axes[1].imshow(arceus_img)
    axes[1].set_title("Opponent is Arceus", fontsize=6)
    axes[1].axis('off')  # Hide axes

    for i in range(0, ATTACKS):
        if battle[i] == "flamethrower":
            axes[i + 2].imshow(flamethrower_img)
            axes[i + 2].set_title("Arceus used Flamethrower", fontsize=6)
            axes[i + 2].axis('off')  # Hide axes
        elif battle[i] == "judgement":
            axes[i + 2].imshow(judgement_img)
            axes[i + 2].set_title("Arceus used Judgement", fontsize=6)
            axes[i + 2].axis('off')  # Hide axes
        elif battle[i] == "splash":
            axes[i + 2].imshow(arceus_img)
            axes[i + 2].set_title("Arceus used Splash", fontsize=6)
            axes[i + 2].axis('off')  # Hide axes
        elif battle[i] == "draco meteor":
            axes[i + 2].imshow(dracometeor_img)
            axes[i + 2].set_title("Arceus used Draco Meteor", fontsize=6)
            axes[i + 2].axis('off')  # Hide axes


    # Add a super title and labels
    fig.suptitle("Battle Started!", fontsize=24, weight="bold", color="red")
    fig.supxlabel("Time", weight="bold")  # Add x-axis label
    fig.supylabel("Turns", weight="bold")  # Add y-axis label

    # Adjust layout and show plot
    fig.tight_layout(rect=[0, 0.05, 1, 0.95])  # Adjust layout to make room for suptitle
    plt.show()


if __name__ == "__main__":
    main()