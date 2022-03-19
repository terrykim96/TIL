def make_list(word):
    word = list(word)
    set_list = []
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            set_list.append(word[i : j])
    set_list.sort(key = len)
    return set_list


def solution(goods):
    answer = []
    
    for i in range(len(goods)):
        tmp = []
        word_list = make_list(goods[i])
        min_len = 10e6
        for j in range(len(word_list)):
            word_tmp = ''.join(word_list[j])
            if min_len >= len(word_tmp):
                other = goods[: i] + goods[i + 1 :]
                flag = True
                for other_word in other:
                    if word_tmp in other_word:
                        flag = False
                if flag == True:
                    tmp.append(word_tmp)
                    min_len = len(word_tmp)
        if not tmp:
            answer.append('None')
        else:
            tmp = set(tmp)
            tmp = list(tmp)
            tmp.sort()
            answer.append(' '.join(tmp))

    return answer