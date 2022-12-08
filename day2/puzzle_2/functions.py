beats = {"A": "B", "B": "C", "C": "A"}
result_points = {"X": 0, "Y": 3, "Z": 6}
choice_points = {"A": 1, "B": 2, "C": 3}

def sumActualScore(file):
    score = 0
    for line in file:
        choice = findChoice(line)
        score += choice_points[choice]
        score += result_points[line[2]]
    return score

def findChoice(line):
    result = line[2]
    if result == "Z":
        return beats[line[0]]
    elif result == "X":
        return beats[beats[line[0]]]
    return line[0]