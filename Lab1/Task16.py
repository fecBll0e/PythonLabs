import datetime
import random
import itertools


def form_schedule(list_):

    random.shuffle(list_)

    groups = [(list_[i] for i in range(4)), (list_[i] for i in range(4, 8)),
              (list_[i] for i in range(8, 12)), (list_[i] for i in range(12, 16))]

    time = datetime.datetime(2021, 9, 15, 15, 30, 1)
    #Подсказка чтобы не забыть
    #datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

    for i, teams in enumerate(groups):
        print(f'{i + 1} GROUP:')
        for team in itertools.combinations(teams, 2):
            print(' - '.join(team) + ' - ' + time.strftime('%d/%m/%Y, %H:%M'))
            time += datetime.timedelta(days=14, hours=random.randrange(9, 24), minutes=random.randrange(0, 60, 5))
            
form_schedule(['Лацио', 'Эспаньол', 'Реал Бетис', 'Аталанта',
                   'Манчестер Юнайтед', 'Локомотив Москва', 'РБ Лейпциг', 'Америка',
                   'Рома', 'Бенфика', 'Хуниор', 'Аль Ахли',
                   'Сантос Лагуна', 'Интер Милан', 'Чжонбук Моторс', 'Вильярреал'])