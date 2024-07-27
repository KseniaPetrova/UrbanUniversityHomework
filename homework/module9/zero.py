import sympy

def is_prime(n):
    if sympy.isprime(n):
        return f'Простое'
    else:
        return f'Составное'

print(is_prime(9))