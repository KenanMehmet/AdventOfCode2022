from pathlib import Path
from puzzle_1.functions import *
from puzzle_2.functions import *

def getSections(file):
    for line in file:
        print(range(int(line[0])))


if __name__ == "__main__":
    """ 
        Puzzle 1: pair of elves are giving sections of the camp to clean, some elfs get 
        sections that fully encompass their paired elf sections, find those pairs

    """
    file = Path(__file__).with_name('puzzle test.txt')
    with file.open('r') as f: