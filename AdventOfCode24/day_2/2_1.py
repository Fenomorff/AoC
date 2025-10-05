safe = 0
increase = True
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        safe_check = True
        parts = line.strip().split(' ')
        parts = list(map(int, parts))
        for i in range(1, len(parts)):
            if (abs(parts[i] - parts[i - 1]) <= 3) and (parts[i] != parts[i - 1]):
                if i == 1:
                    if parts[1] > parts[0]:
                        increase = True
                    else:
                        increase = False
                else:
                    if (increase and parts[i] < parts[i-1]) or (not increase and parts[i] > parts[i-1]):
                        safe_check = False
                        break
            else:
                safe_check = False
                break
        if safe_check:
            safe += 1

print(safe)