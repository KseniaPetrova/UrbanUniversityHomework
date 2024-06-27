marix = [[3, 2, 1],
         [4, 5, 6],
         [7, 8, 9]]
sum_=0  # 17  13
for i in marix:
    for j in i:
        sum_ += j
        break

print(sum_)
sum_ = 0
sum_ += marix[0][0]
sum_ += marix[1][1]
sum_ += marix[2][2]
print(sum_)
sum_ = 0

for i in range(len(marix)):
    sum_ += marix[i][i]
print(sum_)

sum_ = 0
sum_ += marix[0][2]
sum_ += marix[1][1]
sum_ += marix[2][0]
print(sum_)

sum_ = 0
sum_ += marix[-3][-1]
sum_ += marix[-2][-2]
sum_ += marix[-1][-3]
print(sum_)

sum_ = 0
for i in range((0-len(marix)), 0):
    for j in range((0 - len(marix)), 0):
        if i + j == -4:  # это нечестный ход. его придётся вычитать для каждой матрицы
            sum_ += marix[i][j]
            break
print(sum_)  # 13

marix = [[3, 2, 1, 0, 0],
         [0, 7, 4, 5, 6],
         [0, 0, 4, 5, 6],
         [0, 0, 4, 5, 6],
         [7, 8, 9, 1, 1]]
sum_ = 0  # 20 or 16
for i in range(0, len(marix)):
    for j in range(0, len(marix)):
        if i + j == (len(marix) - 1):
            sum_ += marix[i][j]
            break
print(sum_)  # 13
