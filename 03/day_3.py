"""
'oh bother'
 --Winnie the Pooh
"""


def main():
    """pass"""
    # # part 1
    # with open("input_3.txt", "r") as rucksacks:
    #     total = 0
    #     for rucksack in rucksacks:
    #         rucksack = rucksack.strip('\n')
    #         size = len(rucksack)
    #         first = rucksack[0:size//2]
    #         second = rucksack[size//2:]
    #         item = (set(first) & set(second)).pop()
    #         if item.islower():
    #             print(item, ord(item) - 96)
    #             total += ord(item) - 96
    #         else:
    #             print(item, ord(item) - 38)
    #             total += ord(item) - 38
    # print(total)
    # part 2
    flag = 0
    with open("input_3.txt", "r") as rucksacks:
        total = 0
        sack_set = []
        for rucksack in rucksacks:
            rucksack = rucksack.strip('\n')
            sack_set.append(set(rucksack))
            if flag % 3 == 2:
                item = set.intersection(*sack_set).pop()
                sack_set = []
                if item.islower():
                    print(item, ord(item) - 96)
                    total += ord(item) - 96
                else:
                    print(item, ord(item) - 38)
                    total += ord(item) - 38
            flag += 1
    print(total)


if __name__ == "__main__":
    main()
