import time

def cached_with_expiry(expiry_time):
    def decorator(original_function):
        cache = {} # словарь для хранения кеша

        def wrapper(*args, **kwargs):
            key = (*args, *kwargs.items())
            if key in cache:
                cached_value, cached_timestamp = cache[key]
                if time.time() - cached_timestamp < expiry_time:
                    return f"[CACHED] - {cached_value}"

            result = original_function(*args, **kwargs)
            cache[key] = (result, time.time())
            return result

        return wrapper

    return decorator

@cached_with_expiry(expiry_time=5)  # Устанавливаем время кеширования 5 сек
def get_product(x, y):
    return x * y

print(get_product(3, 5))  # Вычисляем в первый раз
print(get_product(2, 5))  # Новое значение
print(get_product(3, 5))  # Во второй раз срабатывает кеш
time.sleep(6)
print(get_product(3, 5))  # Кеш просрочился, поэтому вновь вычисляется значение
print(get_product(3, 5))  # Вновь достаем из кеша