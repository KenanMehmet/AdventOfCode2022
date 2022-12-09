from pathlib import Path

def getSections(file):
    convertIntoInt = lambda string: [int(num) for num in string.split('-')]
    sections = []
    for line in file:
        pairs = line.strip().split(',')
        pairs = list(map(convertIntoInt, pairs))
        if (
            pairs[0][0] >= pairs[1][0] and 
            pairs[0][1] <= pairs[1][1]
            ) or (
            pairs[1][0] >= pairs[0][0] and 
            pairs[1][1] <= pairs[0][1]
        ):
            sections.append(pairs)
    print(sections)
    return len(sections)


if __name__ == "__main__":
    """ 
        Puzzle 1: pair of elves are giving sections of the camp to clean, some elfs get 
        sections that fully encompass their paired elf sections, find those pairs

    """
    file = Path(__file__).with_name('puzzle input.txt')
    with file.open('r') as f:
        print(getSections(f))