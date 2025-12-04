"""solution for day 3 of AoC25 https://adventofcode.com/2025/day/3"""

def read_file(fname):
    """reads file and saves content in list, deviding by comma 

    Args:
        fname (_type_): File Name

    Returns:
       list: list of inputs from file
    """
    with open(fname, "r", encoding='utf-8') as f:
        memory = []
        for line in f:
            memory.append(line.strip())
        return memory


def part_1(banks):
    """solution of part 1 

    Args:
        banks (list): list of banks

    Returns:
        int: answer
    """
    count = 0
    for bank in banks:
        num_1 = 0
        num_2 = 0
        for battery in bank[:-1]:
            num_1 = max(num_1, int(battery))
        rest_of_bank = bank[bank.find(str(num_1)) + 1:]
        for battery in rest_of_bank:
            num_2 = max(num_2, int(battery))
        count += int(str(num_1) + str(num_2))
    return count


def part_2(banks):
    """solution of part 2 

    Args:
        banks (list): list of banks

    Returns:
        int: answer
    """
    count = 0
    for bank in banks:
        nums = ''
        iteration = 11
        last_index = 0
        while iteration >= 0:
            num = 0
            for battery in bank[last_index:len(bank) - iteration]:
                num = max(int(num), int(battery))
            nums += str(num)
            last_index = bank.find(str(num), last_index) + 1
            iteration -= 1
        count += int(nums)
    return count


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
