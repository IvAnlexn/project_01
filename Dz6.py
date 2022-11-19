# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
import random
song1 = random.choice(list(my_favorite_songs.items()))
song2 = random.choice(list(my_favorite_songs.items()))
song3 = random.choice(list(my_favorite_songs.items()))
print(f'Три песни звучат {song1[1]+song2[1]+song3[1]} минут')
