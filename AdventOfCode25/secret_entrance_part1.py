"""solution for 1st day of AoC25"""

def read_file(fname):
    """reads file and saves content in list

    Args:
        fname (_type_): File Name

    Returns:
       list: list of inputs from file
    """
    with open(fname, "r", encoding='utf-8') as f:
        memory_list = []
        for line in f:
            memory_list.append(line.strip())
        return memory_list


def find_zeros(rotations):
    """returns count of all zeros from list of rotations

    Args:
        rotations (_type_): list of rotation

    Returns:
        _type_: count of zeros
    """
    position = 50
    count = 0
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        if direction == 'L':
            position -= distance
        elif direction == 'R':
            position += distance
        if position % 100 == 0 or position == 0:
            count += 1
    return count


def main():
    """
    calls function that reads file and prints count from function that finds
    zeros
    """
    puzzle_input = read_file('AdventOfCode25/input.txt')
    print(find_zeros(puzzle_input))


if __name__ == '__main__':
    main()
