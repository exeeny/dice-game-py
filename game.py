from random_int_generator import RandomIntGenerator
from fair_rand_protocol import FairRandProtocol
from dice_chooser import DiceChooser
from utils import input_options, loading
from table import ProbabilityTable

class Game:
    def __init__(self, dice_set):
        self.dice_set = dice_set
        self.prob_table = ProbabilityTable(self.dice_set)

    def first_move(self):
        print("let's decide who makes the first move\nI selected a random value in the range 0..1")
        computer = RandomIntGenerator(2)
        loading('generating HMAC')
        print(f'HMAC: {computer.hmac}\nTry to guess my selection.')
        while True:
            try:
                user = input_options("0 or 1: ", self.prob_table)
                if user not in (0, 1):
                    raise ValueError
                break
            except ValueError:
                print("❌ Invalid choice. Try again.")
        print(f'your selection: {user}\nmy selection: {computer.num}\nKEY: {computer.key}')
        result = FairRandProtocol(computer.num, user, 2)
        return result.calculate_index()
    
    def roll(self, dice):
        length = len(dice)
        print(f'I selected a random value in the range 0...{length-1} ')
        computer = RandomIntGenerator(length)
        loading('generating HMAC')
        print(f'HMAC: {computer.hmac}')
        while True:
            try:
                user = input_options(f'add your number in range 0...{length-1} (modulo {length}): ', self.prob_table)
                if not (0 <= user < length):
                    raise ValueError
                break
            except ValueError:
                print(f"❌ Invalid choice. Try again.")
        print(f'your selection: {user}\nmy selection: {computer.num}\nKEY: {computer.key}')
        frp = FairRandProtocol(computer.num, user, length)
        index = frp.calculate_index()
        loading('calculating result...')
        print(f'result: {computer.num} + {user} = {index} (mod {length})')
        return index
    
    def print_winner(self,comp_result, user_result):
        print(f"Computer's dice result: {comp_result}\nUser's dice result: {user_result}")
        if user_result > comp_result:
            print(f"{user_result} > {comp_result}\nUser wins!")
        elif user_result < comp_result:
            print(f"{comp_result} > {user_result}\nI win!")
        else:
            print(f"{comp_result} = {user_result}It's a tie!")
        
    def start(self):
        user_goes_first = self.first_move() == 0
        chooser = DiceChooser(self.dice_set, self.prob_table)
        user_dice, computer_dice = chooser.first_roll(user_goes_first)

        print("You go first.")
        user_index = self.roll(user_dice)
        print("It's time for my roll!")
        comp_index = self.roll(computer_dice)

        self.print_winner(computer_dice.search(comp_index), user_dice.search(user_index) )