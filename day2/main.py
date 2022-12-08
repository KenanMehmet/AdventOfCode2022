from pathlib import Path
from puzzle_1.functions import sumScore

if __name__ == "__main__":
    """
        The elves are holding a Rock, Paper, Scissors tournament and we are given a stragety
        guide to win with A, B, C in the first column and X, Y, Z in the second
        the first column is what are opponent is using, and the second is what we will be using,
        you will get a score based on what you use and if you win or not
        1 = Rock, 2 = Paper, 3 = Scizzors, 0 = Loss, 3 = Tie, 6 = Win
    """
    file = Path(__file__).with_name('puzzle test.txt')
    with file.open('r') as f:
        print(sumScore(f))
