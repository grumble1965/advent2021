import sys


class DeterministicDie:
    def __init__(self):
        self._die = 0
        self._counter = 0

    def roll(self):
        self._die += 1
        if self._die > 100:
            self._die = 1
        self._counter += 1
        return self._die

    def count(self):
        return self._counter


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    start_1, start_2 = None, None
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(tmp)
            if start_1 is None:
                start_1 = int(tmp.split()[-1])
            elif start_2 is None:
                start_2 = int(tmp.split()[-1])
    print(f"Player 1 start = {start_1}  Player 2 start = {start_2}")

    die = DeterministicDie()
    space = [None, start_1, start_2]
    score = [None, 0, 0]
    GameOver, turn = False, 1
    while not GameOver:
        d1 = die.roll()
        d2 = die.roll()
        d3 = die.roll()
        new_space = space[turn] + d1 + d2 + d3
        while new_space > 10:
            new_space -= 10
        new_score = score[turn] + new_space
        if new_score >= 1000:
            print(f"Player {turn} rolls {d1}+{d2}+{d3} and moves to space {new_space} for a final score {new_score}")
            loser_score, die_rolled = score[3-turn], die.count()
            print(f"second place score = {loser_score}  die rolled {die_rolled} times  product = {loser_score*die_rolled}")
            GameOver = True
        else:
            print(f"Player {turn} rolls {d1}+{d2}+{d3} and moves to space {new_space} for a total score of {new_score}")
        space[turn] = new_space
        score[turn] = new_score
        turn = 3 - turn


if __name__ == '__main__':
    main()
