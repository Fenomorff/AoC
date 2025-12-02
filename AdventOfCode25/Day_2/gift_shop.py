# pylint: disable=missing-function-docstring
"""solution for 2st part day 2 of AoC25 https://adventofcode.com/2025/day/1"""

def read_file(fname):
    """reads file and saves content in list, deviding by comma 

    Args:
        fname (_type_): File Name

    Returns:
       list: list of inputs from file
    """
    with open(fname, "r", encoding='utf-8') as f:
        memory = f.read()
        memory = memory.split(',')
        return memory


def part_1(ids_list):
    """part 1 solution

    Args:
        ids_list (list): id's from input file

    Returns:
        int: answer
    """
    count = 0
    for id_range in ids_list:
        first_last_id = id_range.split('-')
        fisrt_id, last_id = int(first_last_id[0]), int(first_last_id[1])
        for i in range(fisrt_id,last_id + 1):
            i = str(i)
            middle = len(i)//2
            first_half, second_half = i[:middle], i[middle:]
            if first_half == second_half:
                count += int(i)
    return count


def part_2(ids_list):
    """part 2 solution

    Args:
        ids_list (list): id's from input file

    Returns:
        int: answer
    """
    count = 0
    for id_range in ids_list:
        first_last_id = id_range.split('-')
        fisrt_id, last_id = int(first_last_id[0]), int(first_last_id[1])
        for i in range(fisrt_id,last_id + 1):
            i = str(i)
            if i[0] == '0':
                continue
            for j in range(1, len(i)//2 + 1):
                cursor = 0
                while cursor < len(i) - j:
                    first_half  = i[cursor: cursor + j]
                    second_half = i[cursor + j:cursor + j * 2]
                    if first_half == second_half:
                        cursor += j
                        isinvalid = True
                        continue
                    isinvalid = False
                    break
                if isinvalid:
                    count += int(i)
                    break
    return count


def main():
    """reads file and prints 4 answers and tests for each day"""    
    ids = read_file('AdventOfCode25/Day_2/input.txt')
    testfile = read_file('AdventOfCode25/Day_2/test.txt')
    print(f'Part 1 Test Answer: {part_1(testfile)}')
    print(f'Part 1 Answer: {part_1(ids)}')
    print(f'Part 2 Test Answer: {part_2(testfile)}')
    print(f'Part 2 Answer: {part_2(ids)}')


if __name__ == '__main__':
    main()
