import pandas as pd
from jikanpy import Jikan
from pprint import pprint
# create list of animes

animes = [['naruto', 'action', 'forever', 'series'],
          ['bleach', 'action', 'forever', 'series'],
          ['demon slayer', 'horror', 'medium', 'series'],
          ['Blue Lock', 'sports', 'future content', 'series'],
          ['Baki', 'martial arts', 'long', 'series'],
          ['Tokyo Ghoul', 'action', 'short', 'series'],
          ['Jujutsu Kaisen', 'action/martial arts', 'short', 'series']]

# input mood
# print('What mood are you in?')
# mood = input()

# loop through and find a matching mood
# for anime in animes:
#     if mood == anime[1]:
#         print(f"{mood} anime: {anime[0]} ")

jikan = Jikan()
mushishi = jikan.anime(457)

mushishi_with_eps = jikan.anime(457, extension='episodes')

# pprint(mushishi)

print(mushishi['title'])
print(mushishi['episodes'])


# monday = jikan.schedule(day="monday")
# pprint(monday)

winter_2018 = jikan.season(year=2009, season="winter")
pprint(winter_2018)