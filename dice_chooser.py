import random
from utils import input_options

class DiceChooser:
    def __init__(self, dice_set, pt):
        self.dice_set = dice_set
        self.pt = pt
        self.user_index = None
        self.comp_index = None
        self.user_dice = None
        self.comp_dice = None

    def user_choose(self, excluded_index=None):
        print("🎲 Choose your dice:")
        for i, d in enumerate(self.dice_set.dice):
            if i != excluded_index:
                print(f"{i}. {d}")
        while True:
            try:
                index = input_options("Enter dice number: ", self.pt)
                if index == excluded_index or not (0 <= index < len(self.dice_set.dice)):
                    raise ValueError
                break
            except ValueError:
                print("❌ Invalid choice. Try again.")

        self.user_index = index
        self.user_dice = self.dice_set.dice[index]
        print(f"You chose Dice #{index}: {self.user_dice}")

    def computer_choose(self, excluded_index=None):
        valid_indexes = [i for i in range(len(self.dice_set.dice)) if i != excluded_index]
        index = random.choice(valid_indexes)
        self.comp_index = index
        self.comp_dice = self.dice_set.dice[index]
        print(f"I chose Dice #{index}: {self.comp_dice}")

    def first_roll(self, user_goes_first):
        if user_goes_first:
            self.user_choose()
            self.computer_choose(excluded_index=self.user_index)
        else:
            self.computer_choose()
            self.user_choose(excluded_index=self.comp_index)
        return (self.user_dice, self.comp_dice)