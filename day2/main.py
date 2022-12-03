import random

points = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
    # "A"  Opponent Rock
    # "B"  Opponent Paper
    # "C"  Opponent Scissors
    "Lost": 0,
    "Draw": 3,
    "Won": 6,
}


def get_winner(p1, p2):
    if (p1 == "C" and p2 == "X") or (p1 == "B" and p2 == "Z") or (p1 == "A" and p2 == "Y"):
        return (1, p2)  # Player wins
    elif (p1 == "A" and p2 == "X") or (p1 == "B" and p2 == "Y") or (p1 == "C" and p2 == "Z"):
        return (-1, p2)  # Draw
    else:
        return (0, p2)  # Player loses


def get_points(played):
    (winner, chosen) = get_winner(played[0], played[2])
    win_score = 0
    match winner:
        case -1:
            win_score = points["Draw"]
        case 0:
            win_score = points["Lost"]
        case 1:
            win_score = points["Won"]
    return win_score + points[chosen]


def choose_move(game):
    p1 = game[0]
    p2 = game[2]
    draw = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    win = {
        "A": "Y",
        "B": "Z",
        "C": "X",
    }

    lose = {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }
    match p2:
        case "X":  # Lose
            return f"{p1} {lose[p1]}"
        case "Y":  # Draw
            return f"{p1} {draw[p1]}"
        case "Z":  # Win
            return f"{p1} {win[p1]}"


with open("./input", "r") as f:
    f = f.readlines()
    moves = list(map(choose_move, f))
    player_points = list(map(get_points, moves))
    print(sum(player_points))
