import richdem as rd
import numpy as np

dem = rd.rdarray(np.load('imgs/beauford.npz')['beauford'], no_data=-9999)

rd.FillDepressions(dem, epsilon=True, in_place=True)
accum_d8 = rd.FlowAccumulation(dem, method='D8')
d8_fig = rd.rdShow(accum_d8, zxmin=450, zxmax=550, zymin=550, zymax=450, figsize=(8,5.5), axes=False, cmap='jet')