import richdem as rd
import numpy as np

beau  = rd.rdarray(np.load('imgs/beauford.npz')['beauford'], no_data=-9999)
slope = rd.TerrainAttribute(beau, attrib='slope_riserun')
rd.rdShow(slope, axes=False, cmap='jet', figsize=(8,5.5))