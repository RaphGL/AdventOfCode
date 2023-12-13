from dataclasses import dataclass

@dataclass
class Cube:
    red: int = 0
    blue: int = 0
    green: int = 0

CubeSets = list[Cube]
GamesDict = dict[int, CubeSets]


def read_game_from_file(filename: str) -> GamesDict:
    with open("inputs.txt", "r") as f:
        inputs = f.readlines()

    def str_to_cubeset(set: str) -> CubeSets:
        set = set.split(',')
        cubes: CubeSets = []
        for cube_str in set:
            cube_str = cube_str.split()
            cube = Cube()
            n = int(cube_str[0])
            match cube_str[1]:
                case "blue": cube.blue = n
                case "red": cube.red = n
                case "green": cube.green = n
            cubes.append(cube)
        return cubes

    games: GamesDict = dict()
    for input in inputs:
        input = input.strip().split(':')
        game_id = int(input[0].split()[1])
        sets = input[1].split(';')
        for (i, set) in enumerate(sets):
            sets[i] = str_to_cubeset(set)
        games[game_id] = sets

    return games


class Game:
    def __init__(self, games: GamesDict, max_red, max_green, max_blue) -> None:
        self.games = games
        self.max_blue = max_blue
        self.max_green = max_green
        self.max_red = max_red

    
    def game_is_possible(self, game: list[CubeSets]) -> bool:
        for set in game:
            for cube in set:
                if cube.red > self.max_red: return False
                if cube.green > self.max_green: return False
                if cube.blue > self.max_blue: return False
        return True


    def sum_of_possible_game_ids(self) -> int:
        games = []
        for (game_id, game) in self.games.items():
            if self.game_is_possible(game):
                games.append(game_id)

        return sum(games)


    @staticmethod
    def get_minimum_game_cubeset(game: list[CubeSets]) -> Cube:
        min_cube = Cube()
        for set in game:
            for cube in set:
                if cube.red > min_cube.red: min_cube.red = cube.red
                if cube.green > min_cube.green: min_cube.green = cube.green
                if cube.blue > min_cube.blue: min_cube.blue = cube.blue
        return min_cube


    @staticmethod
    def get_cube_power(cube: Cube) -> int:
        return cube.red * cube.green * cube.blue


    def get_power(self) -> int:
        total_power = 0
        for game in self.games.values():
            mincube = self.get_minimum_game_cubeset(game)
            cube_power = self.get_cube_power(mincube)
            total_power += cube_power
        return total_power


def main():
    games = read_game_from_file("./inputs.txt")
    game = Game(games, 12, 13, 14)
    print(game.sum_of_possible_game_ids())
    print(game.get_power())

if __name__ == "__main__":
    main()
