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
    """returns count of all passes through "0" from list of rotations

    Args:
        rotations (_type_): list of rotation

    Returns:
        _type_: count of zeros
    """
    position = 50
    count_pass = 0
    count_zero = 0
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        if direction == "R":
            new_position = (position + distance) % 100
            cross = (position + distance) // 100
        elif direction == "L":
            new_position = (position - distance) % 100
            cross = (position - distance + 99) // 100
        else:
            return 0
        if new_position == 0:
            count_zero += 1
        count_pass += cross
        position = new_position
    return count_pass, count_zero, count_pass + count_zero


def main():
    """
    calls function that reads file and prints count from function that finds
    passes through "0"
    """
    puzzle_input = read_file('AdventOfCode25/input.txt')
    print(find_zeros(puzzle_input))


if __name__ == '__main__':
    main()
