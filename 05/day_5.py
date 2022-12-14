"""
    '(shrugs)'
    --Ada
"""


def main():
    """pass"""
    with open("input_5.txt", "r") as advent:
        advent = [x.strip('\n') for x in advent]
        print(part_1(advent))


def part_1(advent):
    """ process header then moves """
    # build header
    # print(advent)
    header = []
    moves = []
    flag = True
    for line in advent:
        if flag:
            if line != '':
                header.append(line)
            else:
                flag = False
                continue
        else:
            moves.append(parse_move(line))
    stacks = parse_header(header)
    # pprint(stacks)
    for move in moves:
        # NOTE: lists start at 0, input starts at 1
        # (a, b, c) move a from b to c
        # get blocks to move, pre-reverse to place
        a, b, c = move
        # to_move = list(reversed(stacks[b-1][:a]))
        to_move = list(stacks[b-1][:a])
        # update source
        stacks[b-1] = stacks[b-1][a:]
        # update destination
        stacks[c-1] = to_move + stacks[c-1]
    tops = [stack[0] for stack in stacks]
    return ''.join(tops)



def parse_header(header):
    """ parse the header into something usable """
    header = [x[1:] for x in list(zip(*header[::-1])) if x[0] != ' ']
    header = [[y for y in x if y != ' '][::-1] for x in header]
    return header


def parse_move(line):
    """ parse the moves into lists """
    # [a, b, c] move a from b to c
    return tuple(int(x) for x in line.split()[1::2])


if __name__ == "__main__":
    main()
