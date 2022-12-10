from pathlib import Path

def runCraneOperations(file):
    """Here we will loop through the lines of the file and run the correct functions"""
    stacks = []
    for line in file:
        print(line.strip().split(' '))
        if not line.strip():
            test_stack = [line[n: n + 3] for n in range(0, len(line), 5)]
            print(test_stack)

def moveCrates(file):
    """Follow Move instructions"""

def createStacksArray(file):
    """In the text file, the crates stacks are seperated by an empty line"""


if __name__ == "__main__":
    """ 
        Puzzle 1: Supplies are stored in stacked crates, but the most needed crates are buried, we need to move them
        the crane operator who moves them does them in one go, she does them in these steps
        move 1 from 2 to 1: move one object from stack 2 to stack 1
        After all the instructions, list the top crate of each stack.
    """
    file = Path(__file__).with_name('puzzle test.txt')
    with file.open('r') as f:
        print(moveCrates(f))