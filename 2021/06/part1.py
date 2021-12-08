from typing import List


class LanternFish:
    def __init__(self, initial: List[int]) -> None:
        self.fishes = []
        for i in range(9):
            self.fishes.append(initial.count(i))

    def new_day(self) -> None:
        new_fish = 0
        for i in range(8):
            if i == 0:
                new_fish = self.fishes[i]
            self.fishes[i] = self.fishes[i + 1]

        self.fishes[-1] = new_fish
        self.fishes[6] += new_fish


def main(file_in: str) -> None:
    with open(f"{file_in}.in", "r") as f:
        fishes = [int(x) for x in f.read().rstrip().split(",")]

    lantern_fishes = LanternFish(fishes)
    for _ in range(80):
        lantern_fishes.new_day()

    print(f"{file_in}. Answer: {sum(lantern_fishes.fishes)}")


if __name__ == "__main__":
    main("test")
    main("puzzle")
