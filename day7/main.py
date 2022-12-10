from pathlib import Path
file_tree = {
    "/": {
        "child": {},
        "size": 0
    }
} #Key will be string, have two values, child directories and size of all items

def runCommands(file):
    current_directory = ""
    for line in file.readlines():
        print(current_directory)
        current_directory = interpretLine(line.strip(), current_directory)
        print(file_tree)

def interpretLine(line, current_directory):
    print(line)
    if line[0] == "$":
        command = line[2:]
        if command[0] == "c":
            return runChangeDirectory(command[3:], current_directory)
        else:
            runList(command, current_directory)
    else:
        if line[0] == "d":
            #file_tree[current_directory]
            print("not yet")
        else:
            line = line.split()
            file_tree[current_directory]["size"] += int(line[0])
    return current_directory

def runChangeDirectory(line, current_directory):
    if line != "..":
        return current_directory + line
    if len(current_directory.split()) == 1:
        return "/"
    current_directory.split().pop()
    return ''.join(current_directory)
    

def runList(line, current_directory):
    if current_directory == "":
        return True

if __name__ == "__main__":
    """ 
        Puzzle 1: The device we were given can not update becuase it has not enough space, we need to run through the commands
        listed in the puzzle input, and find out what directory has the most total space to be a canidate for deleting.
    """
    file = Path(__file__).with_name('puzzle test.txt')
    with file.open('r') as f:
        print(runCommands(f))