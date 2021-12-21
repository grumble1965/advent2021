from collections import deque
import sys


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

    initial_game = (0, [start_1, start_2], [0, 0], [])
    print(f"initial game = {initial_game}")
    all_games = deque()
    all_games.append(initial_game)

    winner = [0, 0]
    while all_games:
        print(f"Currently {len(all_games)} in the deque")
        game = all_games.popleft()
        print(f"this game = {game}")
        turn, space, score, rolls = game
        if len(rolls) < 3:
            # insert three new games; one with die=1, one with die=2, one with die=3
            for die in range(1, 4):
                new_rolls = rolls.copy()
                new_rolls.append(die)
                new_game = (turn, space, score, new_rolls)
                # print(f" rolling the die: {new_game}")
                all_games.append(new_game)
        else:
            [d1, d2, d3] = rolls
            new_space = space[turn] + d1 + d2 + d3
            while new_space > 10:
                new_space -= 10
            new_score = score[turn] + new_space
            if new_score >= 21:
                print(f"Player {turn+1} rolls {d1}+{d2}+{d3} and moves to space {new_space} for a final score {new_score}")
                # loser_score, die_rolled = score[3 - turn], die.count()
                # print(f"second place score = {loser_score}  die rolled {die_rolled} times  product = {loser_score * die_rolled}")
                # GameOver = True
                winner[turn] += 1
            else:
                print(f"Player {turn} rolls {d1}+{d2}+{d3} and moves to space {new_space} for a total score of {new_score}")
                fake_space = space.copy()
                fake_space[turn] = new_space
                fake_score = score.copy()
                fake_score[turn] = new_score
                tt = (1 - turn, fake_space, fake_score, [])
                all_games.append(tt)

    total_games = sum(winner)
    print(f"In {total_games} total games, one player won {max(winner)} games")


if __name__ == '__main__':
    main()
