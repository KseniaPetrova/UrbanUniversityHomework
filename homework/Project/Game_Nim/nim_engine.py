from random import randint

# разложить_камни()
# взять_из_кучи(NN, КК)
# положение_камней() - возвращает список [Xx, YY, 22, …] - текущее расположение камней
# есть_конец_игры() - возвращает True если больше ходов сделать нельзя

_holder = []


def put_stones():
    global _holder
    _holder = []
    for _ in range(5):
        _holder.append(randint(1, 20))


# def take_from_a_pile(position, quantity):
#     if 1 <= position <= len(_holder):
#         _holder[position - 1] -= quantity
#         return True
#
#     if _holder[position-1] < quantity:
#         return False
#
#     if position > len(_holder):
#         return False


def take_from_a_pile(position, quantity):
    if 1 <= position <= len(_holder) and (_holder[position-1] >= quantity and position <= len(_holder)):
        _holder[position - 1] -= quantity
        return True
    else:
        return False


def position_stones():
    return _holder


def end_game():
    return sum(_holder) == 0
