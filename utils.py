from time import sleep
from rich.console import Console

def input_options(text, pt):
    while True:
        print('? - help\nx - exit')
        print(text)
        res = input()
        if res == 'x':
            print('👋 goodbye!')
            exit()
        elif res == '?':
            pt.show_table()
        else:
            return int(res)

def loading(message, delay = 1):
    console = Console()
    with console.status(f"[bold green]{message}"):
        sleep(delay)