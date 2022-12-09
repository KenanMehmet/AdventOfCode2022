
def splitGroups(file):
    group = []
    value = 0
    for line in file:
        group.append(line)
        if len(group) == 3:
            value += findBadge(group)
            group = []
    return value


def findBadge(group):
    group.sort(key=len)
    for char in group[0]:
        if char in group[1] and char in group[2]:
            return getCharValue(char)

def getCharValue(char):
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38