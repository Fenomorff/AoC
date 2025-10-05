def read_file(input_file):
    lines = []
    with open(input_file, encoding="utf-8") as file:
        for line in file:
            lines.append(line)
        return lines

def find_safe_reports(reports):
    safe_reports = 0
    line_index = 0
    counter = 0
    pop_index = 0
    while line_index < len(reports):
        safe_check = True
        levels = list(map(int, reports[line_index].strip().split()))
        if counter > 0:
            levels.pop(pop_index)
            pop_index = -1
        if levels[0] > levels[1] and abs(levels[0] - levels[1]) <= 3:
            for i in range(1, len(levels)-1):
                if levels[i] > levels[i+1]:
                    if levels[i] - levels[i+1] <= 3:
                        safe_check = True
                    else:
                        if counter == 0:
                            pop_index = i+1
                            line_index -= 1
                            counter += 1
                        elif counter == 1:
                            pop_index = i
                            line_index -= 1
                            counter += 1
                        elif counter == 2:
                            pop_index = i-1
                            line_index -= 1
                            counter += 1
                        safe_check = False
                        print(f"UNSAVE | {levels} |  line: {line_index+1}")
                        break
                else:
                    if counter == 0:
                            pop_index = i+1
                            line_index -= 1
                            counter += 1
                    elif counter == 1:
                            pop_index = i
                            line_index -= 1
                            counter += 1
                    elif counter == 2:
                            pop_index = i-1
                            line_index -= 1
                            counter += 1
                    safe_check = False
                    print(f"UNSAVE | {levels} |  line: {line_index+1}")
                    break
            if safe_check is True:
                print(f"SAVE   | {levels} |  line: {line_index}")
                safe_reports += 1
        elif levels[0] < levels[1] and abs(levels[0] - levels[1]) <= 3:
            for j in range(1, len(levels)-1):
                if levels[j] < levels[j+1]:
                    if levels[j+1] - levels[j] <= 3:
                        safe_check = True
                    else:
                        if counter == 0:
                            pop_index = j+1
                            line_index -= 1
                            counter += 1
                        elif counter == 1:
                            pop_index = j
                            line_index -= 1
                            counter += 1
                        elif counter == 2:
                            pop_index = j-1
                            line_index -= 1
                            counter += 1
                        print(f"UNSAVE | {levels} |  line: {line_index+1}")
                        safe_check = False
                        break
                else:
                    if counter == 0:
                            pop_index = j+1
                            line_index -= 1
                            counter += 1
                    elif counter == 1:
                            pop_index = j
                            line_index -= 1
                            counter += 1
                    elif counter == 2:
                            pop_index = j-1
                            line_index -= 1
                            counter += 1
                    safe_check = False
                    print(f"UNSAVE | {levels} |  line: {line_index+1}")
                    break
            if safe_check is True:
                safe_reports += 1
                print(f"SAVE   | {levels} |  line: {line_index}")
        else:
            if counter == 0:
                pop_index = 2
                line_index -= 1
                counter += 1
            elif counter == 1:
                pop_index = 1
                line_index -= 1
                counter += 1
            elif counter == 2:
                pop_index = 0
                line_index -= 1
                counter += 1
        line_index += 1
        if pop_index == -1:
            counter = 0
    return safe_reports


def main():
    reports = read_file("input.txt")
    print(find_safe_reports(reports))


if __name__ == '__main__':
    main()
