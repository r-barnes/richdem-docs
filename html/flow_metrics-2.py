accum_rho8 = rd.FlowAccumulation(dem, method='Rho8')
rd.rdShow(accum_rho8, zxmin=450, zxmax=550, zymin=550, zymax=450, figsize=(8,5.5), axes=False, cmap='jet', vmin=d8_fig['vmin'], vmax=d8_fig['vmax'])