'''
Created on 20 de jun de 2017

@author: Gustavo
'''

'''Experiencia com matplotlib'''
import numpy as np
import matplotlib.pyplot as mp

x= np.array([1950, 1960, 1970, 1980, 1990, 2000])
y= np.array([2.200, 2.900, 3.150, 3.750, 4.200, 5.345])

mp.xlabel("X")
mp.ylabel("Y")

#primeiro o x depois o y
mp.plot(x, y)
mp.show()