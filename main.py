
def funk(a: str):
    info = {}
    Buyer = [1, 2, 3, 4, 5]
    if a == 1 or 2:
            if a == 2:
                # # Обработка данных формы
                # username = form.cleaned_data['username']
                # password = form.cleaned_data['password']
                # repeat_password = form.cleaned_data['repeat_password']
                # age = form.cleaned_data['age']

                if a != 2:
                    info['error'] = 'Пароли не совпадают'
                else:
                    user_exists = False
                    # Перебираем всех покупателей и проверяем их имена
                    for buyer in Buyer:
                        if buyer == a:
                            user_exists = True
                            break  # Выходим из цикла, если нашли совпадение

                    if user_exists:
                        info['error'] = 'Пользователь уже существует'
                    else:
                        # Создаем нового покупателя
                        Buyer.append('new Buyer')  # баланс можно установить по умолчанию
                        info['message'] = f"Приветствуем, {username}!"

            else:
                info['error'] = 'Пожалуйста, исправьте ошибки в форме.'
    info['form'] = "первый иф"
    return info, Buyer


print(funk(2))





