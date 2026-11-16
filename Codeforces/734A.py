n = int(input())
games_won = str(input())

anton_won = 0
danik_won = 0

for i in range(len(games_won)):
    if games_won[i] == "A":
        anton_won += 1
    elif games_won[i] == "D":
        danik_won += 1

if anton_won > danik_won:
    print("Anton") 
elif anton_won < danik_won:
    print("Danik")
elif anton_won == danik_won:
    print("Friendship")