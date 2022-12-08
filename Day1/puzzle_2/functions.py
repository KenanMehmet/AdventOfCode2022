
def findTopThree(file):
    sums = []
    count = 0
    for line in file:
        if len(line.strip()) != 0:
            count += int(line.strip())
        else:
            sums.append(count)
    sums.sort(reverse=True)
    return sum(sums[0:3])
