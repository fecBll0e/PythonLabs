passw1 = 'qwerty'
passw2 = '123'
passw3 = 'qwerty_123'
passw4 = 'Qwerty_123'

def check_str_of_pass(password):
    cnt = 0
    if len(password) > 4: cnt += 1
    l_pass = list(password)
    for i, m in enumerate(l_pass):
        print(l_pass[i])  
        if l_pass[i].isupper(): cnt +=1
        if l_pass[i].isdigit(): cnt += 1
    if cnt == 0: print('Ну это прям вообще слабо')
    if cnt >= 1 and cnt <= 3: print('Слабовато')
    if cnt == 4: print('Нормис')
    if cnt > 4: print('Стронг')
    return 0

check_str_of_pass(passw1)
check_str_of_pass(passw2)
check_str_of_pass(passw3)
check_str_of_pass(passw4)