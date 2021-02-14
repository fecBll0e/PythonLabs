text = 'ZZ xcv qqwweerrrrrtyui oppp'

def once(text):
    return list(filter(lambda x: x.isalpha() and text.count(x) == 1, text))

print(once(text))