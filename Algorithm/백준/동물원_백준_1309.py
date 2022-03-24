# 빈 우리와 사자가 있는 우리로 분리한 뒤
# 빈 우리의 수 * 3(없거나, 왼쪽 오른쪽 모두 가능) + 사자가 있는 우리 * 2(없거나 사자랑 먼쪽)

N = int(input())
lion = [0] * (N + 1)
lion[0] = 1
lion[1] = 3
for i in range(2, N + 1):
    lion[i] = (lion[i - 2] + lion[i - 1] * 2) % 9901
print(lion[N])