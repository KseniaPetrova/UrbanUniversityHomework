"""
Задание:
Напишите код, который форматирует строки для следующих сценариев.
Укажите переменные, которые должны быть вставлены в каждую строку:
"""
"""
Использование %:
Переменные: количество участников первой команды (team1_num).
Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
Переменные: количество участников в обеих командах (team1_num, team2_num).
Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
"""
team1_num = 5
print('В команде Мастера кода участников: %s !' % team1_num)

"""
Использование format():
Переменные: количество задач решённых командой 2 (score_2).
Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
Переменные: время за которое команда 2 решила задачи (team1_time).
Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"
"""
score_2 = 42
print("Команда Волшебники данных решила задач: {} !".format(score_2))

"""
Использование f-строк:
Переменные: количество решённых задач по командам: score_1, score_2
Пример итоговой строки: "Команды решили 40 и 42 задач.”
"""
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')

"""
Переменные: исход соревнования (challenge_result).
Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
"""
def challenge_result(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return 'Победа команды Волшебники Данных!'
    else:
        return 'Ничья!'


result = challenge_result(score_1=40, score_2=42, team1_time=6, team2_time=6)
print(f'Результат битвы: {result}!')

"""
Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
"""
tasks_total = 82
time_avg = 1245.2
mean_time = time_avg / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {mean_time:.2f} секунды на задачу!')
