from typing import List


def get_rows(rows: List[List[str]], index: int, default: str) -> List[List[str]]:
    if len(rows) == 1:
        return rows
    zero_rows = []
    one_rows = []
    count = 0
    for row in rows:
        if row[index] == "1":
            count += 1
            one_rows.append(row)
        else:
            count -= 1
            zero_rows.append(row)

    if default == "1":
        if count < 0:
            return zero_rows
        return one_rows
    if count >= 0:
        return zero_rows
    return one_rows


def main(in_file: str) -> None:
    with open(f"{in_file}.in", "r") as f:
        rows = [list(x.rstrip()) for x in f.readlines()]

    oxy_ratings = rows[:]
    co2_ratings = rows[:]

    for index in range(len(rows[0])):
        oxy_ratings = get_rows(oxy_ratings, index, "1")
        co2_ratings = get_rows(co2_ratings, index, "0")

    bin_oxy = int("".join(oxy_ratings[0]), 2)
    bin_co2 = int("".join(co2_ratings[0]), 2)

    print(f"{in_file}, oxy: {bin_oxy}, co2: {bin_co2}, answer: {bin_oxy * bin_co2}")


if __name__ == "__main__":
    main("test")
    main("puzzle")
