"""Деление"""
# при % на 10 получается последняя цифра число
8 % 10 == 8
74 % 10 == 4
312 % 10 == 2
(5415 % 10 == 5) == (5410 + 5)

# при % на 100 получается 2 последнии цифры числа
4563 % 100 == 63
68432 % 100 == 32

# при // на 10 убирается последняя цифра число
8 // 10 == 0
47 // 10 == 4
(68423 // 10 == 6842) == (68420 + 3)

# при // на 100 убираются 2 последнии цифра числа
5321 // 100 == 53
479842 // 100 == 4798
# -----------------------
# как достать разряды
47865 // 1000 % 10 == 7
47865 // 100 % 10 == 8