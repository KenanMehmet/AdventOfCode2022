from pathlib import Path
Tree = {}

def runCommands(file):
    
    for line in file.readlines():
        print(line.strip())

def interpretLine(line):
    if line[0] == "$":
        return True

def runChangeDirectory(line):
    return True

def runList(line):
    return True

if __name__ == "__main__":
    """ 
        Puzzle 1: The device we were given can not update becuase it has not enough space, we need to run through the commands
        listed in the puzzle input, and find out what directory has the most total space to be a canidate for deleting.
    """
    file = Path(__file__).with_name('puzzle test.txt')
    with file.open('r') as f:
        print(runCommands(f))