beats = {"A": "Z", "B": "X", "C": "Y"}
conversion = {"A": "X", "B": "Y", "C": "Z"}

def sumScore(file):
    for line in file:
        print(line)
        if line[2] == beats[line[0]]:
            print("win")
        elif conversion[0] == line[2]:
            print("tie")
        else:
            print("loss")