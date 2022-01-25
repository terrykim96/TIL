T = int(input())
for i in range(T):
    words = input()
    for j in range(2, 12):
        word_list = []
       
        try:
            for k in range(30 // j):

                word_list.append(words[k * j : (k+1) * j])
            
            if len(set(word_list)) == 1:
                print(f'#{i+1} j')
                break
        except:
            continue