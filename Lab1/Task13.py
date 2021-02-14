def extra_enumerate(list_):
    cum = 0
    for i, elem in enumerate(list_):
        cum += elem
        yield (i, elem, cum, round(sum(list_) / 100 * elem, 3))

for i, element, cum, frac in extra_enumerate([1, 3, 4, 2]):
    print(element, cum, frac)