from pathlib import Path
from puzzle_1.functions import findRepeat
from puzzle_2.functions import findBadge, splitGroups

if __name__ == "__main__":
    """ 
        Part1: Find the repeating item in each bag compartment split into halfs
        Part2: Find the badge in the elf groups of 3
    """
    file = Path(__file__).with_name('puzzle input.txt')
    with file.open('r') as f:
        #print(findRepeat(f))
        print(splitGroups(f))