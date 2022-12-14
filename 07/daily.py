"""
    '(shrugs); (sighs wearily)'
    --Me

NOTE:  ok.  see input.txt for the find/replace hacking done.
$ cd /tmp
$ mkdir sigh
$ bash input.txt
$ find ./sigh -type d > dirs.txt
$ find ./sigh -type f > files.txt
programming below builds on this.  input_raw is input as given by advent of code
"""


def main():
    """pass"""
    sizes = {}
    with open("dirs.txt", "r", encoding="UTF-8") as directories:
        directories = [x.strip('\n') for x in directories]
        with open("files.txt", "r", encoding="UTF-8") as files:
            files = [x.strip('\n') for x in files]
            for folder in directories:
                for file in files:
                    filesize = int(file.split()[0])
                    if folder in file:
                        if folder in sizes:
                            sizes[folder] += filesize
                        else:
                            sizes[folder] = filesize
    sizes_1 = dict((k, v) for k, v in sizes.items() if v <= 100000)
    # pprint(sizes_1)
    print("part 1: ", sum(v for k, v in sizes_1.items()))
    # part 2
    raw_total = 0
    with open("input_raw.txt", "r", encoding="UTF-8") as things:
        for line in things:
            if line[0].isdigit():
                raw_total += int(line.split()[0])
    space_to_free = 30000000 - (70000000 - raw_total)
    # print(space_to_free, raw_total)
    sizes = dict((k, v) for k, v in sizes.items() if v > space_to_free)
    # print(sizes)
    print("part 2: ", min(sizes.items(), key=lambda x: x[1]))


if __name__ == "__main__":
    main()
