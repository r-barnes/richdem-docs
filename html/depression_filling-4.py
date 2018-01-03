beau_epsilon         = rd.FillDepressions(beau, epsilon=True, in_place=False)
beau_eps_diff        = beau_epsilon - beau
beaufig_eps_diff     = rd.rdShow(beau_eps_diff, ignore_colours=[0], axes=False, cmap='jet', figsize=(8,5.5))