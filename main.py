import sys
from dice import Dice, DiceSet
from game import Game

def main():
    args = sys.argv[1:]
    if (len(args)<3):
        print("❌ Error: You must provide at least 3 dice.")
        return
    
    dice_set = DiceSet()
    for arg in args:
        try:
            faces = [int(f.strip()) for f in arg.split(',')]
            dice_set.addDice(Dice(faces))
        except:
            print("❌ Error: dice must contain only integers")
            return
        
    new_game = Game(dice_set)
    new_game.start()

if __name__ == "__main__":
    main()