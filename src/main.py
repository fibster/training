import sys
import os
import random


from player import Player
from blackknight import BlackKnight

def main():

    player = Player("Arthur")
    black_knight = BlackKnight("Black Knight")

    print("Player vs Black Knight")
    print(f"Player's health: {player.getHealth()}")
    print(f"Black Knight's health: {black_knight.getHealth()}")
    while player.is_alive() and black_knight.is_alive():
        black_knight.cut_body_part(random.choice(["arm", "leg", "stomach", "head"]))
        player.cut_body_part(random.choice(["arm", "leg", "stomach", "head"]))
        player.take_damage (random.randint(1, 10))
        black_knight.take_damage(random.randint(1, 10))
        player.status()
        black_knight.status()


    if player.is_alive():
            print("Player wins!")
    else:
            print("Black Knight wins!" )        
           

if __name__ == "__main__":
    main()
