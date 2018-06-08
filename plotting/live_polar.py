import matplotlib.pyplot as plt
import matplotlib.animation as animation            #For live plotting

import math

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection='polar', label='ax')
r = [1,1]

img = plt.imread("map.png")

n = 0

def animate(i):
    global n
    angle = 35*math.cos(n)
    n += 0.05
    theta = [math.radians(angle), math.radians(angle) + math.pi]
    ax.clear()
    ax.set_xticklabels(['0', '-45', '90', '45', '0', '-45', '90', '45'])
    ax.set_yticklabels([])
    ax.plot(theta, r)
    ax.set_rmax(1)

ax_im = fig.add_axes([0.1, 0.1, 0.8, 0.8], label='im')
ax_im.imshow(img, alpha = .4)
ax_im.axis('off')

ani = animation.FuncAnimation(fig, animate, interval=25)

plt.show()
