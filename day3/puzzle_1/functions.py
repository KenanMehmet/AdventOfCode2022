
def findRepeat(file):
    for line in file:
        print(len(line))


def getCharValue(char):
    char.swapcase()
    return ord(char) - 64