bank = {1000: 7, 500: 6, 100: 4, 50: 6}

def count(money):
    res = []
    for banknote, amount in bank.items():
        if money < banknote * amount and not amount == 0:
            amount = money // banknote
        elif amount == 0:
            continue
        money -= banknote * amount
        res.append((amount, banknote))
        bank[banknote] = bank.get(banknote) - amount

    if money == 0:
        for i, j in res:
            print(f'{i}*{j}', end=' ')
    else: 
        print('Операция не может быть выполнена!')

count(10350)