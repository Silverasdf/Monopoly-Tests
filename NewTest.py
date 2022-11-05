import random
from Tile import *
from MonopolyFunctions import *
from matplotlib import pyplot as plt

N = 1000000 #Number of rolls

communitycards = []
chancecards = []

board = [Go, Baltic, CommunityChest1, Mediterranean, Income, ReadingR, Oriental, Chance1, Vermont, Connecticut, Jail, StCharles, ElectricU, States, Virginia, PennsylvaniaR, StJames, CommunityChest2, Tennessee, NY, FreeParking, Kentucky, Chance2, Indiana, Illinois, BOR, Atlantic, Ventnor,WaterU,Marvin,GoToJail,Pacific,NC,CommunityChest3,Pennsylvania,ShortLineR,Chance3,ParkPlace,Luxury,Boardwalk]
bucket = {} #map of spaces on board to number of times landed on {tile: int}
curr = 0 #Current Position
doubles = 0
for key in board:
    bucket[key] = 0
for i in range(N):
    num1, num2 = rollDice(), rollDice()
    number = num1 + num2 #Roll, move
    if num1 == num2:
        doubles += 1 
    else:
        doubles = 0
    curr = (curr + number) % len(board)
    bucket[board[curr]] += 1
    #Special cases
    if doubles == 3: #3 Doubles in a row take you to jail
        curr = Jail.position
        doubles = 0
        bucket[board[curr]] += 1
    elif curr == GoToJail.position:
        curr = Jail.position
        bucket[board[curr]] += 1
        N += 1 #Teleporting counts as a roll
        i += 1
    elif board[curr].team == "Chance":
        if len(chancecards) == 0: #Replenishes chance cards
            chancecards = list(range(1, 16))
        rand, chancecards = take(chancecards)
        if rand == 1: #Advance to Boardwalk
            curr = Boardwalk.position
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
        if rand == 2: #Advance to Go
            curr = Go.position
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
        if rand == 3: #Advance to Illinois
            curr = Illinois.position
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
        if rand == 4: #Advance to St. Charles
            curr = StCharles.position
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
        if rand == 5 or rand == 6: #Go to nearest railroad. Basically, the position goes up until reach railroad
            while board[curr].team != "Railroads":
                curr += 1
                curr %= len(board)
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
        if rand == 7: #Go to nearest Utility
            while board[curr].team != "Utilities":
                curr += 1
                curr %= len(board)
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
        if rand == 10: #Go back 3 spaces
            curr = (curr + len(board) - 3) % len(board)
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
        if rand == 11: #Go to Jail
            curr = Jail.position
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
        if rand == 14: #Advance to Reading Railroad
            curr = ReadingR.position
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
    elif board[curr].team == "Community Chest":
        if len(communitycards) == 0: #Replenishes chance cards
            communitycards = list(range(1, 16))
        rand, communitycards = take(communitycards) #Take a card
        if rand == 1: #Advance to Go
            curr = Go.position
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
        if rand == 6: #Go to jail
            curr = Jail.position
            bucket[board[curr]] += 1
            N += 1 #Teleporting counts as a roll
            i += 1
SortedTiles = dict(sorted(bucket.items(), key=lambda item: item[1])) #Sorts everything from least to most landed on
colors = []
scores = {"Brown": 0, "Cyan": 0, "Magenta": 0, "Railroads": 0, "Utilities": 0, "Orange": 0, "Red": 0, "Yellow": 0, "Green": 0, "Blue": 0}
for key in SortedTiles: #What colors all the bars, and goes through and prints to stdout
    print(f"{key.name}: {SortedTiles[key]}")
    colors.append(key.color)
    if key.team in scores:
        scores[key.team] += SortedTiles[key]
print()
scores = dict(sorted(scores.items(), key=lambda item: item[1]))
for key in scores:
    print(f"{key}: {scores[key]}")

names = []
for key in SortedTiles: #Probability Distribution
    SortedTiles[key] /= N
    names.append(key.name)
values = list(SortedTiles.values())
#Plotting
plt.figure(figsize=(25, 25))
f = plt.figure(1)
plt.title("Monopoly Most Landed On Spaces", fontsize = 50)
plt.bar(range(len(SortedTiles)), values, tick_label=names, color = colors)
plt.xticks(rotation='vertical')
plt.xlabel("Space on Board", fontsize = 35)
plt.ylabel("Percentage Landed on", fontsize = 35)
plt.ylim(0.020, 0.061)
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
plt.figure(figsize=(20, 20))
g = plt.figure(2)
plt.title("Best Monopolies by Most Landed On", fontsize = 35)
plt.bar(range(len(scores)), values, tick_label=names, color = colors)
plt.xticks(rotation='vertical')
plt.xlabel("Monopoly", fontsize = 25)
plt.ylabel("Score", fontsize = 25)
plt.ylim(N/33, N/9)
plt.savefig('Scores.png')