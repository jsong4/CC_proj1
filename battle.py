"""
M3: A Markov Distinction
Course: Computational Creativity
Name: Jimmy Song
Date: 17 September 2024

This code displays a simple battle between two Pokemon: Blissey and Arceus.
Blissey, known for having high levels of HP and special defense, will be attacked by an
array of 5 powerful attacks from Arceus, the literal god of all Pokemon.
It uses a first order Markov Chain to decide the order of attacks
from Arceus's four available moves.

In the Battle class:
get_health() return's Blissey's health stat (HP)
get_next_attack() takes in the current attack used by Arceus and returns the
    next attack based on the entered transition matrix
generate_battle() implements the get_next_attack() function to create
    an array of 5 attacks, and it updates Blissey's health stat based on
    the damage assigned to each attack used

Finally,
main() creates a Battle class, inputting a transition matrix for Arceus's moveset.
It then reads all the images needed for the ensuing battle and displays it with
matplotlib. Finally, based on whether the attacks took all of Blissey's health,
it is displayed whether Blissey survived or was defeated.
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
        self.health = STARTING_HEALTH

    def get_health(self):
        return self.health

    def get_next_attack(self, current_attack):
        """Decides which attack will be used against us, based on the current attack used
        Args: current attack (string)
        Returns: a List containning only the next attack"""
        return random.choices(
            self.attacks, 
            weights = [self.transition_matrix[current_attack][next_attack]
                    for next_attack in self.attacks])
    
    def generate_battle(self, current_attack = None, num_attacks = ATTACKS):
        """Generate a sequence of attacks and updates Blissey's health
        Args: current attack (string, optional), defaults to None
              number of attacks used by opponent (int, optional), defaults to ATTACKS = 5
        Returns: a List of performed attacks"""
        if current_attack == None:
            current_attack = random.choice(self.attacks)
        attacks = []
        while len(attacks) < num_attacks:
            # generate next attack and put into list
            next_attack = (self.get_next_attack(current_attack))[0]
            attacks.append(next_attack)
            # Deduct health from Blissey based on attack damage (splash does 0 damage)
            if next_attack == "flamethrower":
                self.health = self.health - 10
            elif next_attack == "judgement":
                self.health = self.health - 50
            elif next_attack == "draco meteor":
                self.health = self.health - 20
            current_attack = next_attack
        return attacks
    
def main():
    test_battle = Battle(
        # transition matrix of opponent's moveset (standard 4 move arsenal)
        # given the current attack, there is a corresponding probability distributiom for the next attack
        {
            "flamethrower": {"flamethrower": 0.3, "judgement": 0.1, "splash": 0.2, "draco meteor": 0.4},
            "judgement": {"flamethrower": 0.2, "judgement": 0.2, "splash": 0.5, "draco meteor": 0.1},
            "splash": {"flamethrower": 0.2, "judgement": 0.1, "splash": 0.4, "draco meteor": 0.3},
            "draco meteor": {"flamethrower": 0.4, "judgement": 0.1, "splash": 0.3, "draco meteor": 0.2}
        }
    )

    # Use the Battle class to generate a list of attacks used by Arceus
    battle = test_battle.generate_battle()

    # Read in all images
    blissey_img = Image.open("/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/blissey.png")
    arceus_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/arceus_normal.png')
    flamethrower_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/Arceus_Flamethrower.webp')
    judgement_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/Arceus_judgement.png')
    splash_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/Arceus_splash.jpeg')
    dracometeor_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/Arceus_dracometeor.png')
    win_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/happy_blissey.jpeg')
    loss_img = Image.open('/Users/jsong4/Downloads/Computational Creativity/CC_proj1/Images/sad_blissey.jpg')

    # Create a figure and axes -- columns equal to number of attacks used + 3,
    # to include the opening Pokemon selection and final result images
    fig, axes = plt.subplots(1, ATTACKS+3, figsize=(15, 4))

    # Display Blissey being chosen
    axes[0].imshow(blissey_img)
    axes[0].set_title("I choose Blissey! HP: 100", fontsize=6)
    axes[0].axis('off')  # Hide axes

    # Display the opponent, Arceus
    axes[1].imshow(arceus_img)
    axes[1].set_title("Opponent is Arceus", fontsize=6)
    axes[1].axis('off')  # Hide axes

    # display the attacks decided by the transition matrix
    for i in range(0, ATTACKS):
        if battle[i] == "flamethrower":
            axes[i + 2].imshow(flamethrower_img)
            axes[i + 2].set_title("Arceus used Flamethrower (-10HP)", fontsize=6)
            axes[i + 2].axis('off')  # Hide axes
        elif battle[i] == "judgement":
            axes[i + 2].imshow(judgement_img)
            axes[i + 2].set_title("Arceus used Judgement (-50HP)", fontsize=6)
            axes[i + 2].axis('off')  # Hide axes
        elif battle[i] == "splash":
            axes[i + 2].imshow(splash_img)
            axes[i + 2].set_title("Arceus used Splash (-0HP)", fontsize=6)
            axes[i + 2].axis('off')  # Hide axes
        elif battle[i] == "draco meteor":
            axes[i + 2].imshow(dracometeor_img)
            axes[i + 2].set_title("Arceus used Draco Meteor (-20HP)", fontsize=6)
            axes[i + 2].axis('off')  # Hide axes
    
    # Blissey survives or gets defeated, depending on health level --> display a corresponding message
    if test_battle.get_health() > 0:
        axes[ATTACKS + 2].imshow(win_img)
        axes[ATTACKS + 2].set_title("Blissey survived! HP: " + str(test_battle.get_health()), fontsize=6, weight="bold")
        axes[ATTACKS + 2].axis('off')  # Hide axes
    else:
        axes[ATTACKS + 2].imshow(loss_img)
        axes[ATTACKS + 2].set_title("Blissey fainted! What did you expect?", fontsize=6, weight="bold")
        axes[ATTACKS + 2].axis('off')  # Hide axes


    # Add a super title and labels
    fig.suptitle("Battle Started!", fontsize=24, weight="bold", color="yellow")
    fig.supxlabel("Time", weight="bold")  # Add x-axis label
    fig.supylabel("Turns", weight="bold")  # Add y-axis label

    # Adjust layout and show plot
    fig.tight_layout(rect=[0, 0.05, 1, 0.95])  # Adjust layout to make room for suptitle
    fig.patch.set_facecolor('xkcd:baby blue')
    plt.show()


if __name__ == "__main__":
    main()