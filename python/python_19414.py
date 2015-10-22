# Setting theta-ticks in matplotlib polar plots
import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax1.set_xticks(np.pi/180. * np.linspace(180,  -180, 8, endpoint=False))
