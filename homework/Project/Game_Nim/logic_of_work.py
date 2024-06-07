# Ним - математическая игра, в которой два игрока по очереди берут предметы,
# разложенные на несколько кучек. За один ход может быть взято любое количество предметов
# (большее нуля) из одной кучки. Выигрывает игрок, взявший последний предмет.
# В классическом варианте игры число кучек равняется трем.
# Составить модуль, реализующий функциональность игры.
# Функции управления игрой
# разложить_камни()
# взять_из_кучи(NN, КК)
# положение_камней() - возвращает список [Xx, YY, 22, …] - текущее расположение камней
# есть_конец_игры() - возвращает True если больше ходов сделать нельзя
# В текущем модуле реализовать логику работы с пользователем:
# начало игры,
# вывод расположения камней
# ввод первым игроком хода -
# позицию и кол-во камней
# вывод расположения камней
# вывод вторым игроком хода - позицию и кол-во камней
# вывод расположения камней


from nim_engine import put_stones, take_from_a_pile, position_stones, end_game
from termcolor import termcolor

put_stones()
termcolor.cprint('Start the game', color='green')
user_number = 1
while True:
    print('Current position')
    print(position_stones())
    print(user_number, ' gamer moves')
    pos = int(input('Enter colum: '))
    qua = int(input('Enter quantity: '))
    step_successed = take_from_a_pile(pos, qua)
    if step_successed:
        if user_number == 1:
            user_number = 2
        else:
            user_number = 1
    else:
        termcolor.cprint('An impossible move', color="red")
        continue
    if end_game():
        break
print('Gameover. The winner is player ', user_number)
