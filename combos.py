#!/usr/bin/env python3
"""Filter valid Killer Sudoku cage combinations by size, sum, excluded, and required digits."""
import argparse
import itertools


def find_combos(cells: int, total: int, exclude: set[int] = set(), include: set[int] = set()) -> list[tuple[int, ...]]:
    out = []
    for c in itertools.combinations(range(1, 10), cells):
        if sum(c) != total:
            continue
        s = set(c)
        if s & exclude:
            continue
        if not include.issubset(s):
            continue
        out.append(c)
    return out


def parse_digits(raw: str) -> set[int]:
    return {int(x) for x in raw.replace(" ", "").split(",") if x.isdigit()}


def main() -> None:
    ap = argparse.ArgumentParser(description="Killer Sudoku cage combination finder")
    ap.add_argument("--cells", type=int, required=True, help="Number of cells in cage (2-9)")
    ap.add_argument("--sum", type=int, required=True, dest="total", help="Target cage sum")
    ap.add_argument("--exclude", default="", help="Comma-separated digits to exclude, e.g. 1,9")
    ap.add_argument("--include", default="", help="Comma-separated digits already in cage, e.g. 4")
    args = ap.parse_args()

    res = find_combos(args.cells, args.total, parse_digits(args.exclude), parse_digits(args.include))
    if not res:
        print("No valid combinations.")
        return
    must = sorted(set.intersection(*(set(c) for c in res)))
    possible = sorted(set.union(*(set(c) for c in res)))
    print(f"Found {len(res)} combination(s):")
    for c in res:
        print(" ", " · ".join(map(str, c)))
    if must:
        print("Must appear:", " · ".join(map(str, must)))
    print("Possible digits:", " · ".join(map(str, possible)))


if __name__ == "__main__":
    main()
