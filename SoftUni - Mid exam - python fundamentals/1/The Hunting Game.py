days_of_adventure = int(input())
count_of_players = int(input())
group_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())
water_for_veryone = water_per_day * count_of_players * days_of_adventure
food_for_everyone = food_per_day * count_of_players * days_of_adventure
flag = True
for day in range(1,days_of_adventure + 1):
    energy_lost = float(input())
    group_energy -= energy_lost
    if group_energy <= 0:
        flag = False
        break
    if day % 2 == 0:
        group_energy += group_energy * 0.05
        water_for_veryone -= water_for_veryone * 0.3
    if day % 3 == 0:
        food_for_everyone -= food_for_everyone / count_of_players
        group_energy += group_energy * 0.1
if flag:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food_for_everyone:.2f} food and {water_for_veryone:.2f} water.")