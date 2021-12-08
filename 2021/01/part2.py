def main():
    with open("puzzle.in", "r") as f:
        puzzle_input = [int(x.rstrip()) for x in f.readlines()]

    count = 0
    current = 0
    for x in range(2, len(puzzle_input)):
        sliding_sum = sum(map(lambda x: x, puzzle_input[x - 2 : x + 1]))
        if sliding_sum > current:
            count += 1
        current = sliding_sum

    print(count - 1)


if __name__ == "__main__":
    main()
