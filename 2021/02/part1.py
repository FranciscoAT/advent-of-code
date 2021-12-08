def main(file: str) -> None:
    depth = 0
    distance = 0
    with open(f"{file}.in") as f:
        for line in f.readlines():
            line = line.rstrip().split(" ")
            command = line[0]
            unit = int(line[1])
            if command == "forward":
                distance += unit
            elif command == "down":
                depth += unit
            else:
                depth -= unit

    print(f"{file}: {depth * distance}")


if __name__ == "__main__":
    main("test")
    main("puzzle")
