from typing import Tuple


class Grid:
    def __init__(self, x, y) -> None:
        self.grid = []
        for _ in range(y + 1):
            self.grid.append([0] * (x + 1))

    def __str__(self) -> str:
        output = ""
        for row in self.grid:
            output += " ".join([str(x) for x in row])
            output += "\n"

        return output

    def draw_path(self, alpha: Tuple[int, int], beta: Tuple[int, int]) -> None:
        alpha_x, alpha_y = alpha
        beta_x, beta_y = beta

        start_x = min(alpha_x, beta_x)
        end_x = max(alpha_x, beta_x)
        start_y = min(alpha_y, beta_y)
        end_y = max(alpha_y, beta_y)

        if start_x == end_x:
            for y in range(start_y, end_y + 1):
                self.grid[y][start_x] += 1
        elif start_y == end_y:
            for x in range(start_x, end_x + 1):
                self.grid[start_y][x] += 1
        else:
            left_x, left_y = alpha if alpha_x < beta_x else beta
            right_x, right_y = alpha if alpha_x > beta_x else beta

            current_y = left_y
            for x in range(left_x, right_x + 1):
                self.grid[current_y][x] += 1
                if left_y > right_y:
                    current_y -= 1
                else:
                    current_y += 1

    def count_overlaps(self) -> int:
        overlaps = 0
        for row in self.grid:
            overlaps += len([x for x in row if x > 1])
        return overlaps


def main(file_in: str) -> None:
    paths = []
    max_x = 0
    max_y = 0
    with open(f"{file_in}.in", "r") as f:
        for line in f.readlines():
            line = line.rstrip()
            coordinates = line.split(" -> ")
            path = []
            for coordinate in coordinates:
                coordinate = coordinate.split(",")
                x = int(coordinate[0])
                if x > max_x:
                    max_x = x
                y = int(coordinate[1])
                if y > max_y:
                    max_y = y
                path.append((x, y))
            paths.append(tuple(path))

    grid = Grid(max_x, max_y)

    for path in paths:
        grid.draw_path(*path)

    print(f"{file_in}. Answer: {grid.count_overlaps()}")


if __name__ == "__main__":
    main("test")
    main("puzzle")
