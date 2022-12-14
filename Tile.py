class Tile:
    def __init__(self, name, color, position, team=""):
        self.name = name
        self.color = color
        if team == "":
            self.team = color
        else:
            self.team = team
        self.position = position

Baltic = Tile("Baltic Avenue", "Brown", 1)
Mediterranean = Tile("Mediterranean Avenue", "Brown", 3)
Oriental = Tile("Oriental Avenue", "Cyan", 6)
Vermont = Tile("Vermont Avenue", "Cyan", 8)
Connecticut = Tile("Connecticut Avenue", "Cyan", 9)
StCharles = Tile("St. Charles Place", "Magenta", 11)
States = Tile("States Avenue", "Magenta", 13)
Virginia = Tile("Virginia Avenue", "Magenta", 14)
StJames = Tile("St. James Avenue", "Orange", 16)
Tennessee = Tile("Tennessee Avenue", "Orange", 18)
NY = Tile("New York Avenue", "Orange", 19)
Kentucky = Tile("Kentucky Avenue", "Red", 21)
Indiana = Tile("Indiana Avenue", "Red", 23)
Illinois = Tile("Illinois Avenue", "Red", 24)
Atlantic = Tile("Atlantic Avenue", "Yellow", 26)
Ventnor = Tile("Ventnor Avenue", "Yellow", 27)
Marvin = Tile("Marvin Gardens", "Yellow", 29)
Pacific = Tile("Pacific Avenue", "Green", 31)
NC = Tile("North Carolina Avenue", "Green", 32)
Pennsylvania = Tile("Pennsylvania Avenue", "Green", 34)
ParkPlace = Tile("Park Place", "Blue", 37)
Boardwalk = Tile("Boardwalk", "Blue", 39)
ReadingR = Tile("Reading Railroad", "Black", 5, "Railroads")
PennsylvaniaR = Tile("Pennsylvania Railroad", "Black", 15, "Railroads")
BOR = Tile("B & O Railroad", "Black", 25, "Railroads")
ShortLineR = Tile("Short Line", "Black", 35, "Railroads")
ElectricU = Tile("Electric Company", "Lightgray", 12, "Utilities")
WaterU = Tile("Water Works", "Lightgray", 28, "Utilities")
Go = Tile("Go", "Darkgray", 0, "Corner")
Jail = Tile("Jail", "Darkgray", 10, "Corner")
GoToJail = Tile("Go to Jail", "Darkgray", 30, "Corner")
FreeParking = Tile("Free Parking", "Darkgray", 20, "Corner")
CommunityChest1 = Tile("Community Chest 1", "Darkgray", 2, "Community Chest")
CommunityChest2 = Tile("Community Chest 2", "Darkgray", 17, "Community Chest")
CommunityChest3 = Tile("Community Chest 3", "Darkgray", 33, "Community Chest")
Chance1 = Tile("Chance 1", "Darkgray", 7, "Chance")
Chance2 = Tile("Chance 2", "Darkgray", 22, "Chance")
Chance3 = Tile("Chance 3", "Darkgray", 36, "Chance")
Luxury = Tile("Luxury Tax", "Darkgray", 38, "Tax")
Income = Tile("Income Tax", "Darkgray", 4, "Tax")