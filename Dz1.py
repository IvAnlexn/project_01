# Задача 1
# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
song1 = my_favorite_songs[:14]
song2 = my_favorite_songs[16:30]
song3 = my_favorite_songs[32:49]
song4 = my_favorite_songs[51:62]
song5 = my_favorite_songs[64:]
print(song1, song5, song2, song4, sep = '\n')
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.