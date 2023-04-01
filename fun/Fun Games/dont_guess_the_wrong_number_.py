import random

numbers = random.randint(1,3)

player_choice = int(input("Chose a number from 1 to 3 ⏳: "))
bomb_computer = int(numbers)

print(f"You chose 😅: {player_choice}")
print(f"Bomb Number 💣is: {bomb_computer}")

if player_choice == bomb_computer:
    print("Oops You Just Exploded 🫨 😵")
else:
    print("You Survived, Congrats 😊")

