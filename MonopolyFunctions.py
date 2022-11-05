import random
def rollDice():
    return random.randint(1, 6)

def take(list):
    tmp = random.randint(1, len(list)) #There are 16 chance and community chest cards. Take one, burn it, use it
    rand = list[tmp-1]
    list.remove(rand)
    return rand, list