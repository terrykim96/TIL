T = int(input())

for test_case in range(1, T + 1):
    words = []
    for _ in range(5):
        words.append(list(map(str, input())))

    max_len = 0
    length = []

    for word in words:
        length.append(len(word))
        if max_len < len(word):
            max_len = len(word)

    ans = ''

    for i in range(max_len):
        for j in range(5):
            if length[j] > i:
                ans += words[j][i]
    
    print(f'#{test_case} {ans}')