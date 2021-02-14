import random

def random_arr():
    n = random.randrange(1, 10000)
    i = 2
    while i < n:
        i *= 2
    list_ = [random.randint(0, 100000) for i in range(1, n+1)]
    while len(list_) < i:
        list_.append(0)
    print('{} {}'.format(n, i))
    return list_

print(random_arr())