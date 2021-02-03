def set_up(word):
    word = word.split()
    for i, w in enumerate(word):
        if w[0].isupper():
            word[i] = w.upper() 
    return ' '.join(word)

print(set_up('Dfkjd, dfsdf . Sdfs'))