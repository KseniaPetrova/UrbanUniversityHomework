'https://stepik.org/lesson/1319385/step/4?unit=1334766'

def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, dict):
            for key, value in res.items():
                if isinstance(key, str):
                    res[key] = key.upper()
        elif isinstance(res, (list, set, tuple)):
            res = type(res)(elem.upper() if isinstance(elem, str) else elem for elem in res)
        return res

    return wrapper

@uppercase_elements
def my_func():
    return ['monarch', 'Touch', 'officiaL', 'DangerouS', 'breathe']

print(my_func())




