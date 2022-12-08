from pathlib import Path
from functions import findTopThree

if __name__ == "__main__":
    """Find the top 3 elves with the most snacks in calories and their total amount"""
    file = Path(__file__).with_name('puzzle input.txt')
    with file.open('r') as f:
        print(findTopThree(f))