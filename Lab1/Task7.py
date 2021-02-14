def checker(w):
    if w.startswith('www.'):
        w = 'http://' + w
    if not w.endswith('.com'):
        w += '.com'
    return w

word = 'dsafsdf www.fsvsdfvsd www.sdfsdfvsd.com'.split()
print(list(map(checker, word)))