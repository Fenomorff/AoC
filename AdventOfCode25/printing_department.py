"""solution for day 4 of AoC25 https://adventofcode.com/2025/day/4"""

def read_file(fname):
    """reads file and saves content in list, deviding by comma 

    Args:
        fname (string): File Name

    Returns:
       list: list of inputs from file
    """
    with open(fname, "r", encoding='utf-8') as f:
        memory = []
        for line in f:
            memory_row = []
            line = line.strip()
            for item in line:
                memory_row.append(item)
            memory.append(memory_row)
        return memory


def part_1(rows):
    """solution of part 1
    
    Args:
        rows (list): list of rows 

    Returns:
        int: answer
    """
    answer = 0
    counter = 0
    for row in range(0, len(rows)):
        for item in range(0, len(rows[row])):
            if rows[row][item] == '@':
                ## top
                if row:
                    if rows[row - 1][item] == '@':
                        counter += 1
                    ## topleft
                    if item:
                        if rows[row - 1][item - 1] == '@':
                            counter += 1
                    ## topright
                    if item != len(rows[row]) - 1:
                        if rows[row - 1][item + 1] == '@':
                            counter += 1
                ## left
                if item:
                    if rows[row][item - 1] == '@':
                        counter += 1
                ## right
                if item != len(rows[row]) - 1:
                    if rows[row][item +1] == '@':
                        counter += 1
                ## bottom
                if row != len(rows) - 1:
                    if rows[row + 1][item] == '@':
                        counter += 1
                    ## bottomleft
                    if item:
                        if rows[row + 1][item - 1] == '@':
                            counter += 1
                    ## bottomright
                    if item != len(rows[row]) - 1:
                        if rows[row + 1][item + 1] == '@':
                            counter += 1
                if counter < 4:
                    answer += 1
                counter = 0
    return answer


def part_2(rows):
    """solution of part 2
    
    Args:
        rows (list): list of rows

    Returns:
        int: answer
    """
    answer = 0
    counter = 0
    cycle_answer = 1
    while cycle_answer:
        cycle_answer = 0
        for row in range(0, len(rows)):
            for item in range(0, len(rows[row])):
                if rows[row][item] == '@':
                    ## top
                    if row:
                        if rows[row - 1][item] == '@':
                            counter += 1
                        ## topleft
                        if item:
                            if rows[row - 1][item - 1] == '@':
                                counter += 1
                        ## topright
                        if item != len(rows[row]) - 1:
                            if rows[row - 1][item + 1] == '@':
                                counter += 1
                    ## left
                    if item:
                        if rows[row][item - 1] == '@':
                            counter += 1
                    ## right
                    if item != len(rows[row]) - 1:
                        if rows[row][item +1] == '@':
                            counter += 1
                    ## bottom
                    if row != len(rows) - 1:
                        if rows[row + 1][item] == '@':
                            counter += 1
                        ## bottomleft
                        if item:
                            if rows[row + 1][item - 1] == '@':
                                counter += 1
                        ## bottomright
                        if item != len(rows[row]) - 1:
                            if rows[row + 1][item + 1] == '@':
                                counter += 1
                    if counter < 4:
                        cycle_answer += 1
                        rows[row][item] = '.'
                    counter = 0
        answer += cycle_answer
    return answer


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
