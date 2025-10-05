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


    def search_x_mas(text):
        """
        search for double "M" "A" "S" combination in specific X-shaped case in given text
        :param text: input text
        :return: count of matches
        """
        x_mas = 0
        for i in range(len(text)):
            print(f'row {i}: {text[i]}')
            for j in range(len(text[i])):
                print(f'character {i}|{j}: {text[i][j]}')
                if text[i][j] == 'M':
                    print(f'looking for x_mas...')
                    # check if our first M is bottom right and second M, if existing, is bottom left
                    if j >= 2 and text[i][j - 2] == 'M':
                        if i >= 2 and text[i - 1][j - 1] == 'A':
                            if text[i - 2][j] == 'S' and text[i-2][j - 2] == 'S':
                                print('X_MAS FOUND. M\'s: BOTTOM RIGHT; BOTTOM LEFT')
                                x_mas += 1
                    # check if our first M is bottom right and second M, if existing, is upper right
                    if i >= 2 and text[i - 2][j] == 'M':
                        if j >= 2 and text[i - 1][j - 1] == 'A':
                            if text[i - 2][j - 2] == 'S' and text[i][j - 2] == 'S':
                                print('X_MAS FOUND. M\'s: BOTTOM RIGHT; UPPER RIGHT')
                                x_mas += 1
                    # # check if our first M is bottom right and second M, if existing, is upper left
                    # if i >= 2 and j >= 2 and text[i - 2][j - 2] == 'M':
                    #     if text[i - 1][j - 1] == 'A':
                    #         if text[i - 2][j] == 'S' and text[i][j - 2] == 'S':
                    #             print('X_MAS FOUND. M\'s: BOTTOM RIGHT; UPPER LEFT')
                    #             x_mas += 1
                    # check if our first M is bottom left and second M, if existing, is upper left
                    if i >= 2 and text[i - 2][j] == 'M':
                        if j < len(text[i]) - 2 and text[i - 1][j + 1] == 'A':
                            if text[i - 2][j + 2] == 'S' and text[i][j + 2] == 'S':
                                print('X_MAS FOUND. M\'s: BOTTOM LEFT; UPPER LEFT')
                                x_mas += 1
                    # # check if our first M is bottom left and second M, if existing, is upper right
                    # if i >= 2 and j < len(text[i]) - 2 and text[i - 2][j + 2] == 'M':
                    #     if text[i - 1][j + 1] == 'A':
                    #         if text[i - 2][j] == 'S' and text[i][j + 2] == 'S':
                    #             print('X_MAS FOUND. M\'s: BOTTOM LEFT; UPPER RIGHT')
                    #             x_mas += 1
                    # check if our first M is upper right and second M, if existing, is upper left
                    if j >= 2 and text[i][j - 2] == 'M':
                        if i < len(text) - 2 and text[i + 1][j - 1] == 'A':
                            if text[i + 2][j] == 'S' and text[i + 2][j - 2] == 'S':
                                print('X_MAS FOUND. M\'s: UPPER RIGHT; UPPER LEFT')
                                x_mas += 1
        return x_mas


    def main():
        text = read_file('input.txt')
        print(search_x_mas(text))


    if __name__ == '__main__':
        main()