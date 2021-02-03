try:
    money = float(input("Введите вещественное число: "))
except ValueError as e:
    print('Некорректный формат!', e)
else:
	paper = int(money)
	coins = int((money-paper)*100)
	print("{} руб. {} коп.".format(paper, coins))