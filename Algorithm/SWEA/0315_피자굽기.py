from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = deque(enumerate(list(map(int, input().split())), 1))
    oven = deque()

    for _ in range(N):
        oven.append(pizza.popleft())

    while len(oven) > 1:
        if len(oven) < N and pizza:
            oven.append(pizza.popleft())
        idx, tmp = oven.popleft()

        if not tmp // 2:
            continue
        else:
            oven.append((idx, tmp // 2))
    print(f'#{test_case} {oven.popleft()[0]}')