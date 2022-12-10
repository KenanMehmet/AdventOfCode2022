from pathlib import Path

def detectMarker(file):
    unique_chars = []
    read = file.read()
    chars = 0
    for char in read:
        chars += 1
        unique_chars.append(char)
        if len(unique_chars) == 4:
            if len(set(unique_chars)) == len(unique_chars):
                return chars
            unique_chars.pop(0)


if __name__ == "__main__":
    """ 
        Puzzle 1: Create a subroutine for the broken communicator that detects the start of packet marker in the message
        the packet marker is determined as the first 4th different character in the sequences of characters

        Puzzle 2: 
    """
    file = Path(__file__).with_name('puzzle input.txt')
    with file.open('r') as f:
        print(detectMarker(f))