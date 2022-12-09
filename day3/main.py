from pathlib import Path
from puzzle_1.functions import findRepeat
from puzzle_2.functions import findBadge, splitGroups

if __name__ == "__main__":
    """ Find the elf holding the most snacks in calories"""
    file = Path(__file__).with_name('puzzle input.txt')
    with file.open('r') as f:
        #print(findRepeat(f))
        print(splitGroups(f))