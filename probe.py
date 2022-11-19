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
songs_lenght = [3.03, 4.02, 3.40, 3.03, 5.28, 4.15, 4.04, 2.58, 4.02]
random_lenght = random.choices(list(songs_lenght, k = 3))
print(random_lenght)