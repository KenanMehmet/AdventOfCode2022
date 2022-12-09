from pathlib import Path
from puzzle_1.functions import findRepeat

if __name__ == "__main__":
    """ Find the elf holding the most snacks in calories"""
    file = Path(__file__).with_name('puzzle test.txt')
    with file.open('r') as f:
        print(findRepeat(f))