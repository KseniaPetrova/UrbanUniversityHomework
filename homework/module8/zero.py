n, k = map(int, input().split())
# n и k (1 ≤ n ≤ 10, 1 ≤ k ≤ 240)
a = 240 - k  # 'а' времени остаётся на n задач
b = 0  # время потраченное на задачи
#t = 5  # 5 минут на первую задачу
r = 0  # количество решенных задач
while b < a:
    for i in range(1, n+1):
        b = b + i * 5
        if b <= a:
            r += 1
        else:
            break
    if r >= n:
        break
print(r)
