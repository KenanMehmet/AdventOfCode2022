from pathlib import Path
from functions import findMax

if __name__ == "__main__":
    """ Find the elf holding the most snacks in calories"""
    file = Path(__file__).with_name('puzzle input.txt')
    with file.open('r') as f:
        print(findMax(f))