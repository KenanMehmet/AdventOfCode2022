beats = {"A": "Z", "B": "X", "C": "Y"}
conversion = {"A": "X", "B": "Y", "C": "Z"}
choice_points = {"X": 1, "Y": 2, "Z": 3}

def sumScore(file):
    score = 0
    for line in file:
        score += choice_points[line[2]] 
        if line[2] == beats[line[0]]:
            continue
        elif conversion[line[0]] == line[2]:
            score += 3
        else:
            score += 6
    return score