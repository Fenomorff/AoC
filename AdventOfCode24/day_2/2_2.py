def line_check(parts, safe_check_counter):
    """
    Checks list for monotonic sequence, difference within range, and without consecutive repetitions. Allow elimination
    of one number in list if it's allows to convert unsafe list into safe.
    :param parts:
        list of numbers for checking
    :param safe_check_counter:
        counter of safe checks for repeated safe checks with elimination of one level
    :return:
        'UNSAFE' if list not passing checks even with elimination of one level
        'SAFE' if list passing without elimination of one level
        'SEMI-SAFE' if passed with elimination of one level
    """
    i = 1
    increase = True
    while i < len(parts):
        if (abs(parts[i] - parts[i - 1]) <= 3) and (parts[i] != parts[i - 1]):
            if i == 1:
                if parts[1] > parts[0]:
                    increase = True
                else:
                    increase = False
                i += 1
            else:
                if (increase and parts[i] < parts[i - 1]) or (not increase and parts[i] > parts[i - 1]):
                    if safe_check_counter == 1:
                        return 'UNSAFE'
                    else:
                        for j in range(len(parts)):
                            safe_check_counter = 1
                            mod_parts = parts.copy()
                            mod_parts.pop(j)
                            status = line_check(mod_parts, safe_check_counter)
                            match status:
                                case 'UNSAFE':
                                    if j == len(parts):
                                        return 'UNSAFE'
                                    continue
                                case 'SAFE':
                                    return 'SEMI-SAFE'
                else:
                    i += 1
        else:
            if safe_check_counter == 1:
                return 'UNSAFE'
            else:
                for j in range(len(parts)):
                    safe_check_counter = 1
                    mod_parts = parts.copy()
                    mod_parts.pop(j)
                    status = line_check(mod_parts, safe_check_counter)
                    match status:
                        case 'UNSAFE':
                            if j == len(parts) - 1:
                                return 'UNSAFE'
                            continue
                        case 'SAFE':
                            return 'SEMI-SAFE'
    return "SAFE"


def main():
    safe = 0
    line_index_counter = 0
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            parts = list(map(int, parts))
            line_index_counter += 1
            status = line_check(parts, 0)
            match status:
                case 'UNSAFE':
                    print(f'UNSAFE: {parts} | {line}')
                    print(f'Safe Reports: {safe} | line index: {line_index_counter}')
                case 'SAFE':
                    safe += 1
                    print(f'SAFE: {parts} | {line}')
                    print(f'Safe Reports: {safe} | line index: {line_index_counter}')
                case 'SEMI-SAFE':
                    safe += 1
                    print(f'SEMI-SAFE: {parts} | {line}')
                    print(f'Safe Reports: {safe} | line index: {line_index_counter}')




if __name__ == '__main__':
    main()


