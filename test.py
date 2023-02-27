from Tree import Tree
from evolve import mutate, crossover, tournament
from random import randrange

#### TODO: test tournament

dicto = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
gen = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
size = 5
print(dicto)
print(gen)
print(tournament(gen, size, dicto))