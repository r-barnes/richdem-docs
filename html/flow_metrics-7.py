metrics = (
  ('D8',       accum_d8      ),
  ('Rho8',     accum_rho8    ),
  ('Dinf',     accum_dinf    ),
  ('Quinn',    accum_quinn   ),
  ('Holmgren', accum_holmgren),
  ('Freeman',  accum_freeman )
)

subr = lambda x: x[450:550,450:550]

fig, axs = plt.subplots(nrows=2, ncols=3)

#Flatten list
axs = [item for sublist in axs for item in sublist]

vmin, vmax = np.nanpercentile(subr(accum_d8), [2, 98])

for i, met in enumerate(metrics):
  axs[i].imshow(subr(met[1]), vmin=vmin, vmax=vmax, cmap='jet')
  axs[i].set_title(met[0])

plt.tight_layout()
plt.show()