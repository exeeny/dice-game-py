class Dice:
    def __init__(self, faces):
        self.faces = faces

    def __len__(self): 
        return len(self.faces)
    
    def __iter__(self):
        return iter(self.faces)

    def search(self, index):
        return self.faces[index]

    def __str__(self):
        return f"{self.faces}" 
    
class DiceSet:
    def __init__(self):
        self.dice = []

    def addDice(self, dice):
        self.dice.append(dice)