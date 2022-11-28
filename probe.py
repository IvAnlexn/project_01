def generator():
    simbols = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    try:
        dlinap = int(input('Введите длину пароля...'))
    except:
        dlinap = int(input('Вы ввели не число!\nВведите коректную длину пароля...'))
    x = list()
    import random
    for i in range(dlinap):
        x.append(random.choice(simbols))
    print(f'Ваш пароль - {"".join(x)}')
generator()