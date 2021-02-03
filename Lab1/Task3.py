hide_num = ''
card = str(input('Введите номер карты (16 цифр): '))
for i in range(16):
	if i < 12 and i > 3:
		hide_num += '*'
	else: hide_num += card[i]
print(hide_num)	