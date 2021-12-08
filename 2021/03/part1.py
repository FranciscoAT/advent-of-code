def main(in_file: str) -> None:
    with open(f"{in_file}.in", "r") as f:
        rows = [list(x.rstrip()) for x in f.readlines()]

    counts = [0] * len(rows[0])
    for row in rows:
        row = map(int, row)
        for index, x in enumerate(row):
            if x == 1:
                counts[index] += 1
            else:
                counts[index] -= 1

    bin_gamma = ""
    bin_epsilon = ""
    for x in counts:
        if x > 0:
            bin_gamma += "1"
            bin_epsilon += "0"
        else:
            bin_gamma += "0"
            bin_epsilon += "1"

    bin_gamma = int(bin_gamma, 2)
    bin_epsilon = int(bin_epsilon, 2)

    print(
        f"{in_file}, gamma: {bin_gamma}, epsilon: {bin_epsilon}, answer: {bin_gamma * bin_epsilon}"
    )


if __name__ == "__main__":
    main("test")
    main("puzzle")
