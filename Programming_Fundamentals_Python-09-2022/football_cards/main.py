cards = input()
disqualified_a = set()
disqualified_b = set()
disqualified_players = cards.split(" ")
terminated = False

for i in disqualified_players:
    team_number = i.split("-")
    if team_number[0] == "A":
        disqualified_a.add(team_number[1])
    else:
        disqualified_b.add(team_number[1])

    if len(disqualified_a) > 4 or len(disqualified_b) > 4:
        terminated = True
        break

print(f"Team A - {11-len(disqualified_a)}; Team B - {11-len(disqualified_b)}")
if terminated:
    print("Game was terminated")
