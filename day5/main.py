from pathlib import Path

def runCraneOperations(file):
    """Here we will loop through the lines of the file and run the correct functions"""
    stacks = []
    stacks_made = False
    for line in file.readlines():
        if not stacks_made:
            stacks, stacks_made = createStacksArray(stacks, line)
        else:
            moveAllCrates(line, stacks)
    top_crates = [stack[-1][1] for stack in stacks]
    return ''.join(top_crates)


def moveCrates(line, stacks):
    """Follow Move instructions"""
    line = line.split()
    origin_stack = stacks[int(line[3]) - 1]
    new_stack = stacks[int(line[5]) - 1]
    for i in range(int(line[1])):
        new_stack.append(origin_stack[-1])
        origin_stack.pop()

def createStacksArray(stacks, line):
    """In the text file, the crates stacks are seperated by an empty line"""
    if len(line.strip()) == 0:
        for stack in stacks:
            stack.reverse()
        return [stacks, True]
    line = line[0:-1] #Cull the /n but keep the spaces
    line_splited = [line[n: n + 4] for n in range(0, len(line), 4)]
    if len(stacks) == 0:
        stacks = [[] for i in range(len(line_splited))]
    for i in range(len(line_splited)):
        if line_splited[i][0] == "[":
            stacks[i].append(line_splited[i])
    return [stacks, False]

def moveAllCrates(line, stacks):
    """Follow Move instructions"""
    line = line.split()
    origin_stack = stacks[int(line[3]) - 1]
    new_stack = stacks[int(line[5]) - 1]
    crates = origin_stack[-(int(line[1])):]
    for crate in crates:
        new_stack.append(crate)
        origin_stack.pop()

if __name__ == "__main__":
    """ 
        Puzzle 1: Supplies are stored in stacked crates, but the most needed crates are buried, we need to move them
        the crane operator who moves them does them in one go, she does them in these steps
        move 1 from 2 to 1: move one object from stack 2 to stack 1
        After all the instructions, list the top crate of each stack.

        Puzzle 2: The Crane moves all crates in one go, update code accordingly
    """
    file = Path(__file__).with_name('puzzle input.txt')
    with file.open('r') as f:
        print(runCraneOperations(f))