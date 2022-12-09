
def findRepeat(file):
    #repeats_value = 0
    repeats = []
    for line in file:
        half_point = int(len(line.strip()) / 2)
        first_compartment = line[0:half_point]
        second_compartment = line[half_point:]
        for char in first_compartment:
            if char in second_compartment:
                print(char)
                print(second_compartment)
                #repeats_value += getCharValue(char)
                repeats.append([char, getCharValue(char)])
                break
    print(repeats)
    #return repeats_value

def getCharValue(char):
    print(char)
    print(ord(char))
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38