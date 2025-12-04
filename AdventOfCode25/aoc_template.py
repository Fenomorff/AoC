"""solution for day _ of AoC25 https://adventofcode.com/2025/day/_"""

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
    
def part_1(items):
    """solution of part 1 

    Args:
        banks (list): list of banks

    Returns:
        int: answer
    """


def part_2(items):
    """solution of part 1 

    Args:
        banks (list): list of banks

    Returns:
        int: answer
    """


def main():
    """calls function that reads file and prints count from function that finds

    """
    puzzle_input = read_file('input.txt')
    testfile = read_file('test.txt')
    print(f'First Part Test: {part_1(testfile)}')
    print(f'First Part Answer: {part_1(puzzle_input)}')
    print(f'Second Part Test: {part_2(testfile)}')
    print(f'Second Part Answer: {part_2(puzzle_input)}')

if __name__ == '__main__':
    main()
