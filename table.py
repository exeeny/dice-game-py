from rich.console import Console
from rich.table import Table

class ProbabilityTable:
    def __init__(self, dice_set):
        self.dice_set = dice_set
        self.table = self.build_table()

    def calculate_win_probability(self, d1, d2):
        win_count = 0
        total_outcomes = len(d1)*len(d2)
        for n1 in d1:
            for n2 in d2:
                if n1 > n2:
                    win_count +=1
        return win_count / total_outcomes

    def build_table(self):
        dice_list = self.dice_set.dice
        labels = [f"{dice_list[i]}" for i in range(len(dice_list))]
        table = Table(title="❓ Dice Win Probabilities", header_style="bold magenta")
        table.add_column("Dice", style="dim")
        for label in labels:
            table.add_column(label)
        for i, label_row in enumerate(labels):
            row = [label_row]
            for j in range(len(dice_list)):
                if i == j:
                    prob = self.calculate_win_probability(dice_list[i], dice_list[j])
                    row.append(f"— {prob:.5f}")
                else:
                    prob = self.calculate_win_probability(dice_list[i], dice_list[j])
                    row.append(f"{prob:.5f}")
            table.add_row(*row)
        return table
    
    def show_table(self):
        console = Console()
        console.print(self.table)