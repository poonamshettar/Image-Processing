import numpy as np
import matplotlib.pyplot as plt
import cv2



image=cv2.imshow('images\\assignment_im.jpg')
# image_2d = np.random.rand(100, 100)
# Plot the 2D image
plt.imshow(image, cmap='gray')
plt.show()
x = np.arange(0, 100)
y = np.arange(0, 100)
x, y = np.meshgrid(x, y)

# The z coordinate is the intensity of the pixel
z = image
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)

# Show the plot
plt.show()

