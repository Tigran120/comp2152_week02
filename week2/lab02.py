import random
weapon = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
wp_strength = [1, 2, 3, 4, 5, 6]

weaponRoll = random.randint(1, 6)

heroStrength = 10
heroStrength += wp_strength[weaponRoll - 1]
print(f"Hero's weapon: {weapon[weaponRoll - 1]}")
print(f"Hero's total strength: {heroStrength}")

if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if weaponRoll != 1:
    print("Thank goodness you didn't roll the Fist...")

print("\nOptional: Try a manual roll!")
user_input = input("Enter a number between 1 and 6: ")

if user_input.isdigit():
    user_roll = int(user_input)
    if 1 <= user_roll <= 6:
        heroStrength = 10 + wp_strength[user_roll - 1]
        print(f"\nYou manually selected: {weapon[user_roll - 1]}")
        print(f"Hero's total strength: {heroStrength}")

        if user_roll <= 2:
            print("You rolled a weak weapon, friend.")
        elif user_roll <= 4:
            print("Your weapon is meh.")
        else:
            print("Nice weapon, friend!")

        if user_roll != 1:
            print("Thank goodness you didn't roll the Fist...")
    else:
        print("Error: The number must be between 1 and 6.")
else:
    print("Error: Please enter a valid number between 1 and 6.")