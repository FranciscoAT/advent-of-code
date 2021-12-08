from typing import Optional


class Board:
    def __init__(self) -> None:
        self.rows = []
        self.board_map = {}

    def __str__(self) -> str:
        output = ""
        for row in self.rows:
            output += " ".join([str(x) for x in row])
            output += "\n"

        return output

    def add_row(self, str_row: str) -> None:
        new_row = []
        for x in str_row.split(" "):
            try:
                new_row.append(int(x))
            except Exception:
                continue

        row_number = len(self.rows)
        for index, x in enumerate(new_row):
            location = (row_number, index)
            if x not in self.board_map:
                self.board_map[x] = [location]
            else:
                self.board_map[x].append(location)

        for index, x in enumerate(new_row):
            new_row[index] = (False, x)

        self.rows.append(new_row)

    def bingo(self, number: int) -> Optional[int]:
        if number not in self.board_map:
            return None

        for location in self.board_map[number]:
            self.rows[location[0]][location[1]] = (True, number)

        # Check horizontal
        for row in self.rows:
            if False not in [x[0] for x in row]:
                return self._get_unmarked_sum()

        # Check vertical
        for i in range(len(self.rows[0])):
            if False not in [row[i][0] for row in self.rows]:
                return self._get_unmarked_sum()

        return None

    def _get_unmarked_sum(self) -> int:
        unmarked_sum = 0
        for row in self.rows:
            unmarked_sum += sum([x[1] for x in row if x[0] is False])
        return unmarked_sum


def main(file_in: str) -> None:
    numbers = []
    boards = []
    current_board = None
    with open(f"{file_in}.in", "r") as f:
        for index, line in enumerate(f.readlines()):
            line = line.rstrip()
            if index == 0:
                numbers = [int(x) for x in line.split(",")]
            elif not line:
                if current_board is not None:
                    boards.append(current_board)
                current_board = Board()
            elif current_board is not None:
                current_board.add_row(line)

    boards.append(current_board)

    for number in numbers:
        for board in boards:
            if (bingo := board.bingo(number)) is not None:
                print(board)
                print(
                    f"{file_in}, bingo: {bingo}, number: {number}. Answer: {bingo * number}"
                )
                return


if __name__ == "__main__":
    main("test")
    main("puzzle")
