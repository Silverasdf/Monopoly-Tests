import random
from matplotlib import pyplot as plt
def rollDice():
    return random.randint(1, 6)

N = 1000000 #Number of rolls

communitycards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
chancecards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

board = ["Go", "Baltic", "CommunityChest1", "Mediterranean", "Income", "ReadingR", "Oriental", "Chance1", "Vermont", "Connecticut", "Jail", "St. Charles", "ElectricU", "States", "Virginia", "PennsylvaniaR", "StJames", "CommunityChest2", "Tennessee", "New York", "Free Parking", "Kentucky", "Chance2", "Indiana", "Illinois", "B&OR","Atlantic","Ventnor","WaterU","Marvin","GotoJail","Pacific","NC","CommunityChest3","Pennsylvania","ShortLineR","Chance3","ParkPlace","Luxury","Boardwalk"]
bucket = {} #map of spaces on board to number of times landed on
curr = 0 #Current Position
for key in board:
    bucket[key] = 0
for i in range(N):
    number = rollDice() + rollDice() #Roll, move
    curr += number
    curr %= len(board)
    bucket[board[curr]] += 1
    #Special cases
    if board[curr] == "GotoJail":
        curr = 10
    if board[curr] == "Chance1" or board[curr] == "Chance2" or board[curr] == "Chance3":
        if len(chancecards) == 0: #Replenishes chance cards
            chancecards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        tmp = random.randint(1, len(chancecards)) #There are 16 chance and community chest cards. Take one, burn it, use it
        rand = chancecards[tmp-1]
        chancecards.remove(rand)
        if rand == 1: #Advance to Boardwalk
            curr = 39
        if rand == 2: #Advance to Go
            curr = 0
        if rand == 3: #Advance to Illinois
            curr = 24
        if rand == 4: #Advance to St. Charles
            curr = 11
        if rand == 5 or rand == 6: #Go to nearest railroad. Basically, the position goes up until reach railroad
            string = board[curr]
            while string[-1] != 'R':
                curr += 1
                curr %= len(board)
                string = board[curr]
        if rand == 7: #Go to nearest Utility
            string = board[curr]
            while string[-1] != 'U':
                curr += 1
                curr %= len(board)
                string = board[curr]
        if rand == 10: #Go back 3 spaces
            curr -= 3
            if curr < 0:
                curr = 39
        if rand == 11: #Go to Jail
            curr = 10
        if rand == 14: #Advance to Reading Railroad
            curr = 5
    if board[curr] == "CommunityChest1" or board[curr] == "CommunityChest2" or board[curr] == "CommunityChest3":
        if len(communitycards) == 0: #Replenishes community cards
            communitycards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        tmp = random.randint(1, len(communitycards)) #There are 16 chance and community chest cards. Take one, burn it, use it
        rand = communitycards[tmp-1]
        communitycards.remove(rand)
        if rand == 1: #Advance to Go
            curr = 0
        if rand == 6: #Go to jail
            curr = 10
sort_by_value = dict(sorted(bucket.items(), key=lambda item: item[1])) #Sorts everything from least to most landed on
colors = []
scores = {"Brown": 0, "Cyan": 0, "Magenta": 0, "Railroads": 0, "Utilities": 0, "Orange": 0, "Red": 0, "Yellow": 0, "Green": 0, "Blue": 0}
for key in sort_by_value: #What colors all the bars, and goes through and prints to stdout
    print(f"{key}: {sort_by_value[key]}")
    if key == "Baltic" or key == "Mediterranean":
        colors.append("Brown")
        scores["Brown"] += sort_by_value[key]
    elif key[-1] == "R":
        colors.append("Black")
        scores["Railroads"] += sort_by_value[key]
    elif key[-1] == "U":
        colors.append("LightGray")
        scores["Utilities"] += sort_by_value[key]
    elif key == "Oriental" or key == "Vermont" or key == "Connecticut":
        colors.append("Cyan")
        scores["Cyan"] += sort_by_value[key]
    elif key == "St. Charles" or key == "States" or key == "Virginia":
        colors.append("Magenta")
        scores["Magenta"] += sort_by_value[key]
    elif key == "StJames" or key == "Tennessee" or key == "New York":
        colors.append("Orange")
        scores["Orange"] += sort_by_value[key]
    elif key == "Kentucky" or key == "Indiana" or key == "Illinois":
        colors.append("Red")
        scores["Red"] += sort_by_value[key]
    elif key == "Atlantic" or key == "Ventnor" or key == "Marvin":
        colors.append("Yellow")
        scores["Yellow"] += sort_by_value[key]
    elif key == "Pacific" or key == "NC" or key == "Pennsylvania":
        colors.append("Green")
        scores["Green"] += sort_by_value[key]
    elif key == "ParkPlace" or key == "Boardwalk":
        colors.append("Blue")
        scores["Blue"] += sort_by_value[key]
    else:
        colors.append("Darkgray")
scores = dict(sorted(scores.items(), key=lambda item: item[1]))
for key in scores:
    print(f"{key}: {scores[key]}")
names = list(sort_by_value.keys())
values = list(sort_by_value.values())

#Plotting
f = plt.figure(1)
plt.title("Monopoly Most Landed On Spaces")
plt.bar(range(len(sort_by_value)), values, tick_label=names, color = colors)
plt.xticks(rotation='vertical')
plt.xlabel("Space on Board")
plt.ylabel("Number of times landed")
plt.ylim(N/55, N/33)
plt.savefig('Spaces.png')

#Plot2
colors = []
for key in scores:
    if key == "Railroads":
        colors.append("Black")
    elif key == "Utilities":
        colors.append("Lightgray")
    else:
        colors.append(key)
names = list(scores.keys())
values = list(scores.values())
g = plt.figure(2)
plt.title("Best Monopolies by Most Landed On")
plt.bar(range(len(scores)), values, tick_label=names, color = colors)
plt.xticks(rotation='vertical')
plt.xlabel("Monopoly")
plt.ylabel("Score")
plt.ylim(N/33, N/9)
plt.savefig('Scores.png')