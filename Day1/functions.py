
def findMax(file):
    count = 0
    max = 0
    for line in file:
        if len(line.strip()) != 0:
            count += int(line.strip())
        else:
            if count > max:
                max = count
            count = 0
    return max