# N = int(input())
# cards = [i for i in range(1, N+1)]

# while len(cards) > 1:
#     cards.pop(0)     # 먼저 제일 앞 카드를 버린다.

#     num = cards.pop(0)  # 그 후 앞에 있는 카드를 맨뒤로 옮긴다.
#     cards.append(num)
    
# print(cards[0])

# 리스트 사용하면 시간초과 떠서 deque 사용
from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while len(deque) > 1:
    deque.popleft()     # 먼저 제일 앞 카드를 버린다.

    num = deque.popleft()   # 그 후 앞에 있는 카드를 맨뒤로 옮긴다.
    deque.append(num)
    
print(deque[0])