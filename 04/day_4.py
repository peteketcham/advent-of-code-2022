"""
'I'm a sheep!  I'm a sheep!  I'm a sheep!'
 --June
"""


def main():
    """pass"""
    with open("input_4.txt", "r") as ranges:
        ranges = [x.strip('\n') for x in ranges]
        # rucksack = rucksack.strip('\n')
        print(part_1(ranges))


def part_1(ranges):
    """ docstring what? """
    count = 0
    for assignment_pairs in ranges:
        assignment_pairs = parse_range(assignment_pairs)
        # if inside(assignment_pairs):
        if inside_2(assignment_pairs):
            count +=1
    return count


def inside_2(pairs):
    """ part deux """
    one = pairs[0]
    two = pairs[1]
    # two[0] between one
    if two[0] >= one[0] and two[0] <= one[1]:
        return True
    # two[1] between one
    if two[1] >= one[0] and two[1] <= one[1]:
        return True
    # one[0] between two
    if one[0] >= two[0] and one[0] <= two[1]:
        return True
    # one[1] between two
    if one[1] >= two[0] and one[1] <= two[1]:
        return True
    return False
    
    
    
def inside(pairs):
    """ docstring lol """
    one = pairs[0]
    two = pairs[1]
    # one inside of two
    if one[0] >= two[0] and one[1] <= two[1]:
        return True
    if two[0] >= one[0] and two[1] <= one[1]:
        return True
    return False


def parse_range(text):
    """
    example pairs:
    "2-4,6-8" -> [(2,4), (6,8)]
    2-3,4-5
    """
    text = text.split(",")
    result = []
    for thing in text:
        result.append(tuple(int(x) for x in thing.split("-")))
    return result

if __name__ == "__main__":
    main()
