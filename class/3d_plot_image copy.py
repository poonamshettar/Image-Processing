import numpy as np
import matplotlib.pyplot as plt
import cv2

image=cv2.imread('images\\assignment_im.jpg',0)
print(image.shape)
# Plot the 2D image
plt.imshow(image, cmap='gray')
plt.show()
x = np.arange(0, 820)
y = np.arange(0, 724)
x, y = np.meshgrid(x, y)

# The z coordinate is the intensity of the pixel
z = image
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,cmap='gray')

# Show the plot
plt.show()

