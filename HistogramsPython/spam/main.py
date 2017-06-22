'''
Created on 22 de jun de 2017

@author: Gustavo
'''

import matplotlib.pyplot as plt
import numpy as np

ar=np.random.random_integers(45, 300, 200)

plt.hist(ar, 30)
plt.show()