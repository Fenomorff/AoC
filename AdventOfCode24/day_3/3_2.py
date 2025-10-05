# script that takes memory input text file, adds to it "do()" in the start and "don't()" in the and,
# split it in segments between "do()" and "don't()" strips all corrupt segments, makes list of correct memory,
# than takes numbers from "mul(expression1,expression2)" template, multiplies, and prints product

import re


def read_file(fname):
    """
    Read a text file and return a string of memory
    :param fname: file name
    :return: string content
    """
    with open(fname, encoding='utf-8') as f:
        memory_list = ''
        for line in f:
            memory_list += line.strip()
        return memory_list


def main():
    memory = read_file("input.txt")
    memory = 'do()' + memory + 'don\'t()'
    print(memory)

    segmented_memory = re.findall(r'do\(\).+?don\'t\(\)', memory)
    print(segmented_memory)
    print(len(segmented_memory))

    clean_memory = []
    for item in segmented_memory:
        clean_memory.append(re.findall(r'mul\([0-9]+,[0-9]+\)', item))
    print(clean_memory)

    memory_nums = []
    for segment in clean_memory:
        for item in segment:
            memory_nums.append(re.findall(r'[0-9]+',
                                      str(item)))

    products = 0
    for nums in memory_nums:
        nums = list(map(int, nums))
        products += nums[0] * nums[1]
    print(products)


if __name__ == '__main__':
    main()
