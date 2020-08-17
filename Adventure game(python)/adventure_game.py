import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def game_intro(weapon, kill_weapon, enemy):
    print_pause(
        "You find yourself standing in an open field, "
        "filled with grass and yellow wildflowers.")
    print_pause(
        "Rumor has it that a wicked fairie is somewhere around here, "
        "and has been terrifying the nearby village.\n")
    ask_choice(weapon, kill_weapon, enemy)


def ask_choice(weapon, kill_weapon, enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = valid_input(input("(Please enter 1 or 2).\n"))
    if choice == "1":
        house(weapon, kill_weapon, enemy)
    else:
        cave(weapon, kill_weapon, enemy)


def valid_input(choice):
    if choice == "1" or choice == "2":
        return choice
    else:
        choice = input("(Please enter 1 or 2).\n")
        valid_input(choice)


def cave(weapon, kill_weapon, enemy):
    print_pause("You peer cautiously into the cave.\n")
    if kill_weapon in weapon:
        print_pause(
            "You've been here before, and gotten all the good stuff. "
            "It's just an empty cave now.\n")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {kill_weapon} of Ogoroth!")
        print_pause(f"You discard your silly old {weapon[0]} and take "
                    f"the {kill_weapon} with you.\n")
        weapon.append(kill_weapon)
    print_pause("You walk back out to the field\n")
    ask_choice(weapon, kill_weapon, enemy)


def house(weapon, kill_weapon, enemy):
    print_pause("You approach the door of the house.")
    print_pause(
        f"You are about to knock when the door opens and out steps "
        f"a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!\n")
    if kill_weapon not in weapon:
        print_pause(
            f"You feel a bit under-prepared for this, what with only "
            f"having a tiny {weapon[0]}.")
        decision = valid_input(
            input("Would you like to (1) fight or (2) run away?\n"))
        if decision == "1":
            print_pause("You do your best...")
            print_pause(f"but your {weapon[0]} is no match for the {enemy}.")
            print_pause("You have been defeated!\n")
            play_again(weapon, kill_weapon, enemy)
        else:
            print_pause(
                "You run back into the field. Luckily, you don't seem to "
                "have been followed.\n")
            ask_choice(weapon, kill_weapon, enemy)
    else:
        decision = valid_input(
            input("Would you like to (1) fight or (2) run away?\n"))
        if decision == "1":
            print_pause(
                f"As the {enemy} moves to attack, you unsheath your new"
                f" {kill_weapon}.")
            print_pause(
                f"The {kill_weapon} of Ogoroth shines brightly in your "
                "hand as you brace yourself for the attack.")
            print_pause(
                f"But the {enemy} takes one look at your shiny new toy "
                "and runs away!")
            print_pause(
                f"You have rid the town of the {enemy}. You are victorious!\n")
            play_again(weapon, kill_weapon, enemy)
        else:
            print_pause(
                "You run back into the field. Luckily, you don't seem to have "
                "been followed.\n")
            ask_choice(weapon, kill_weapon, enemy)


def play_again(weapon, kill_weapon, enemy):
    play_choice = valid_text_input()
    if play_choice == 'y':
        print_pause("Excellent! Restarting the game ...\n")
        initialize(weapon)
    else:
        print_pause("Thanks for playing! See you next time.\n")


def valid_text_input():
    choice = input("Would you like to play again? (y/n)\n")
    if choice == "y" or choice == "n":
        return choice
    else:
        valid_text_input()


def choose_weapon():
    small_weapons = ["dagger", "slicer", "rod"]
    small_weapon = random.choice(small_weapons)
    return (small_weapon)


def choose_kill_weapon():
    kill_weapons = ["sword", "gun", "chopper"]
    kill_weapon = random.choice(kill_weapons)
    return(kill_weapon)


def weapon_clear():
    weapon.clear()
    return(weapon)


def choose_enemy():
    enemies = ["gorgon", "troll", "pirate"]
    enemy = random.choice(enemies)
    return(enemy)


def initialize(weapon):
    weapon.clear()
    small_weapon = choose_weapon()
    kill_weapon = choose_kill_weapon()
    enemy = choose_enemy()
    weapon.append(small_weapon)
    game_intro(weapon, kill_weapon, enemy)


weapon = []
initialize(weapon)
