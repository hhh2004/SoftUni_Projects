days = int(input())
players = int(input())
energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())
water = players * water_per_day_per_person * days
food = players * food_per_day_per_person * days

for i in range(days):
    chopping_energy = (float(input()))
    energy -= chopping_energy
    if energy > 0:
        if i % 2 == 1:
            water *= 0.7
            energy *= 1.05
        if i % 3 == 2:
            food -= food/players
            energy *= 1.1

if energy > 0:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")
