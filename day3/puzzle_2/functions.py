
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
    print(group)
    group.sort(key=len)
    print(group)
    for elf in group:
        print(len(elf))

