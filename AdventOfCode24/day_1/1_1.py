
def convert_file_to_list():

    list_1 = []
    list_2 = []
    with open('input.txt', 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('   ')
            list_1.append(parts[0])
            list_2.append(parts[1])

    list_1 = list(map(int, list_1))
    list_2 = list(map(int, list_2))

    return list_1, list_2


def find_distance(list_1, list_2):
    distance = 0
    for i in range(len(list_1)):
        distance += abs(min(list_1) - min(list_2))
        list_1.remove(min(list_1))
        list_2.remove(min(list_2))

    return distance


def main():
    list_1, list_2 = convert_file_to_list()
    print(find_distance(list_1, list_2))

if __name__ == '__main__':
    main()