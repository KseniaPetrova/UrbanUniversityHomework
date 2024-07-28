"""Цель задания:
Практически применить знания о механизмах блокировки потоков в Python, используя класс Lock из модуля threading.

Задание:
Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.

Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег. Необходимо
использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса."""

from threading import Thread, Lock

class BankAccount:

    def __init__(self, balance):
        self.balance = balance
        self.lock = Lock()

    def deposit(self, amount):
        try:
            self.lock.acquire()
            self.balance += amount
            print(f'Баланс пополнился на {amount} рублей. Теперь на вашем счету {self.balance} рублей')
        finally:
            self.lock.release()

    def withdraw(self, amount):
        with self.lock:
            if amount > self.balance:
                print('Недостаточно средств')
            elif amount <= self.balance:
                self.balance -= amount
                print(f'Вы потратили {amount} рублей. На вашем счету {self.balance} рублей')



def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount(50)

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()