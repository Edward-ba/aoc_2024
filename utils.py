def find_words(word: str, data: list[str]) -> int:
    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == word[0]:
                for rr in [-1, 0, 1]:
                    if rr * (len(word)-1) + i < 0 or rr * (len(word)-1) + i < 0 >= len(data):
                        continue
                    for cc in [-1, 0, 1]:
                        if cc*(len(word)-1) + j < 0 or cc*(len(word)-1) + j >= len(data[0]):
                            continue
                        test = data[i][j]
                        try:
                            for k in range(1, len(word)):
                                test += data[rr*k + i][cc*k + j]
                        except IndexError:
                            continue
                        if test == word:
                            total += 1
    return total
