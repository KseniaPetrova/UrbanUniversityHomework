v = int(input('enter v: '))
sum_v = 0
cout = 0
while v > sum_v:
    a = int(input('something: '))
    sum_v += a
    if sum_v > v:
        sum_v -= a
        break
    cout += 1
print('Довольно!')
print(sum_v)
print(cout)
