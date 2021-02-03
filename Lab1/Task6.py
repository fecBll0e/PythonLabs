def chek_for_symb(word, chek_str, result):
    for j, k in enumerate(chek_str):
        for i, w in enumerate(word):
            if k == w:
                result += ' '.join(chek_str[j])
    print(result)
    for i, w1 in enumerate(result):
        for j, w2 in enumerate(result):
            if w1 == w2 and i != j:
                del result[i] #Shit. Не могу придумать ничего нормального для удаления
    return result
                     
chek_str = '. , ! ? - ; :'.split()
word = input()
result = []
print(chek_for_symb(word, chek_str, result))