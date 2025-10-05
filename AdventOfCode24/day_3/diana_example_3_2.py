import re

def read_file(input_file):
    with open(input_file, encoding="utf-8") as file:
        content = file.read()
        content = 'do()' + content + "don't()"
    return content

def get_mul_pairs(text):
    mul_sequences_list = []
    do_sequences = re.findall(r"(?s)do\(\).+?don't\(\)", text)
    for do_sequence in do_sequences:
        mul_sequences = re.findall(r"mul\(\d+,\d+\)", do_sequence)
        for mul_sequence in mul_sequences:
            mul_sequences_list.append(mul_sequence)
    numbers = list(map(lambda s: s.replace("mul", ""), mul_sequences_list))  
    mul_pairs = []
    for nums in numbers:
        pair = nums.strip('()').split(',')
        mul_pairs.append(pair)
    return mul_pairs

def calculate_result(multiply_pairs):
    result = 0
    for pair in multiply_pairs:
        pair = list(map(int, pair))
        a, b = pair
        product = a * b
        result += product
    return result

def main():
    content = read_file("input-2.txt")
    pairs = get_mul_pairs(content)
    print(calculate_result(pairs))

if __name__ == "__main__":
    main()