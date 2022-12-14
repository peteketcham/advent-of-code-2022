"""
    '(shrugs)'
    --Ada
"""


def main():
    """pass"""
    with open("input.txt", "r", encoding="UTF-8") as advent:
        advent = [x.strip('\n') for x in advent]
        print(part_1(advent))


def part_1(advent):
    """Day 6, part 1

    Args:
        advent (list[str]): lines from file
    """
    marker_length = 14
    for signal in advent:
        for i in range(len(signal) - marker_length + 1):
            if len(set(signal[i : i + marker_length])) == marker_length:
                return i+marker_length
    return 0


if __name__ == "__main__":
    main()
