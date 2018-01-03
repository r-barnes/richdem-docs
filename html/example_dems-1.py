import richdem as rd
import numpy as np

beau = rd.rdarray(np.load('imgs/beauford.npz')['beauford'], no_data=-9999)

rd.rdShow(beau, ignore_colours=[0], axes=False, cmap='jet', figsize=(8,5.5))