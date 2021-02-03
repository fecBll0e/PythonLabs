def sequence(seq):
    for i in reversed(range(len(word))):
        if len(word[i]) > seq:
            res.append(word.pop(i))
    return seq

res = []
word = input().split()
word.reverse()
for i in (7,4,0):
    sequence(i)
print(res)