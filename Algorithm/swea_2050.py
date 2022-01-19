alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

input_alpha = input()

for alpha in input_alpha:
    for i in range(len(alphabet)):
        if alpha == alphabet[i]:
            print(i+1, end = ' ')