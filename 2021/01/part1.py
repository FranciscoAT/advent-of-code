def main():
    with open("puzzle.in", "r") as f:
        input = [int(x.rstrip()) for x in f.readlines()]

    current = 0
    count = 0
    for x in input:
        if x > current:
            count += 1
        current = x

    print(count - 1)


if __name__ == "__main__":
    main()
