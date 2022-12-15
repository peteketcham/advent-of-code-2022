"""
    'It's your choice.  We can go to the donut shop or you can take a break.'
    --Ada
"""

from pprint import pprint

def main():
    """pass"""
    ticker = [1, 1]
    cycle_count = [20, 60, 100, 140, 180, 220]
    with open("input.txt", "r", encoding="UTF-8") as file:
        file = [x.strip("\n") for x in file]
        # file = test
        for line in file:
            tmp = line.split()
            if tmp[0] == "noop":
                ticker.append(ticker[-1])
            if tmp[0] == "addx":
                ticker.append(ticker[-1])
                ticker.append(ticker[-1] + int(tmp[1]))
    total = [ticker[x]*x for x in cycle_count]
    # print(ticker)
    print(total, sum(total))
    # part 2
    screen = []
    for index, value in enumerate(ticker):
        if abs(value - index % 40 + 1)  <= 1:
            screen.append("#")
        else:
            screen.append(".")
    pprint(list(''.join(x) for x in chunkstring(screen[1:], 40)))
    # print(ticker[40:79])


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


if __name__ == "__main__":
    main()
