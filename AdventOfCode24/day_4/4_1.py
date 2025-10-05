def read_file(fname):
    """
    Read a text file and return a string
    :param fname: file name
    :return: string content
    """
    with open(fname, encoding='utf-8') as f:
        text = f.read()
        text = text.split('\n')
        return text


def search_xmas(text):
    """
    search for "X" "M" "A" "S" combination in given text
    :param text: input text
    :return: count of matches
    """
    xmas = 0
    for i in range(len(text)):
        print(f'row: {i}: {text[i]}')
        for j in range(len(text[i])):
            print(f'character: {j}: {text[i][j]}')
            if text[i][j] == 'X':
                print(f'looking for xmas...')
                # west
                if j > 2 and text[i][j - 1] == 'M':
                    if text[i][j - 2] == 'A':
                        if text[i][j - 3] == 'S':
                            print(f'CODE RED: WESTERN HORIZONTAL XMAS TIME!!!!!!!!!')
                            xmas += 1
                # east
                if j < (len(text[i]) - 3) and text[i][j + 1] == 'M':
                    if text[i][j + 2] == 'A':
                        if text[i][j + 3] == 'S':
                            print(f'HOUSTON, HOUSTON: EASTERN XMAS TIME!!!!!!!!!!')
                            xmas += 1
                # scanning row 'above'
                if i > 2:
                    # north
                    if text[i - 1][j] == 'M':
                        if text[i - 2][j] == 'A':
                            if text[i - 3][j] == 'S':
                                print(f'HOLY MOLLY: NORTHERN XMAS TIME!!!!!!!!!!!')
                                xmas += 1
                   # north-west
                    if j > 2 and text[i - 1][j - 1] == 'M':
                        if text[i- 2][j - 2] == 'A':
                            if text[i - 3][j - 3] == 'S':
                                print(f'oh no kanye west daughter... anyway... XMAS TIME!!!!!!!!!!!')
                                xmas += 1
                    # north-east
                    if j < (len(text[i]) - 3) and text[i - 1][j + 1] == 'M':
                        if text[i - 2][j + 2] == 'A':
                            if text[i - 3][j + 3] == 'S':
                                print(f'HAHAHAHAHA IT\'S FREAKING NORTH-EASTERN XMAS TIME!!!!!!!!!!!')
                                xmas += 1
                # scanning row 'below'
                if i < (len(text) - 3):
                    # south
                    if text[i + 1][j] == 'M':
                        if text[i + 2][j] == 'A':
                            if text[i + 3][j] == 'S':
                                print(f'THEY KILLED... someone from southern park, I forgot. XMAS TIME!!!!!!!!!!!')
                                xmas += 1
                    # south-west
                    if j > 2 and text[i + 1][j - 1] == 'M':
                        if text[i + 2][j - 2] == 'A':
                            if text[i + 3][j - 3] == 'S':
                                print(f'yeah okay xmas we get it okay okay it\'s now what, south-western xmas? okay??')
                                xmas += 1
                    # south-east
                    if j < (len(text[i]) - 3) and text[i + 1][j + 1] == 'M':
                        if text[i + 2][j + 2] == 'A':
                            if text[i + 3][j + 3] == 'S':
                                print(f'УВАГА ПІВДЕННО СХІДНЕ РІЗДВО ВІТАЮ ВАС!!!!!')
                                xmas += 1
    return  xmas


def main():
    text = read_file('input.txt')
    print(search_xmas(text))


if __name__ == '__main__':
    main()