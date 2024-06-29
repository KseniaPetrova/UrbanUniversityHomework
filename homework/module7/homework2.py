name = 'poem.txt'
with open(name, encoding='utf-8') as file:
    for line in file:
        print(line, end='') 