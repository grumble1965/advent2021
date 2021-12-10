import sys
from queue import LifoQueue

error_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
match_table = {')': '(', ']': '[', '}': '{', '>': '<'}

def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    error_score = 0
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"read line {tmp}")

            counter = {'paren': 0, 'bracket': 0, 'curly_brace': 0, 'angle_brace': 0}
            wrong_char = None
            stack = LifoQueue(maxsize=9999)
            for ch in tmp:
                # print(f"{ch}", end='')
                if ch in ['(', '[', '{', '<']:
                    stack.put(ch)
                elif ch in [')', ']', '}', '>']:
                    if stack.empty():
                        wrong_char = ch
                        break
                    else:
                        tos = stack.get_nowait()
                        if tos != match_table[ch]:
                            wrong_char = ch
                            break
            # print()

            if wrong_char is not None:
                error_score += error_table[wrong_char]

    print(f"Error score = {error_score}")


if __name__ == '__main__':
    main()
