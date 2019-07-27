import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# =============================================================================
# CUSTOMIZING PLOTS
# =============================================================================

import matplotlib.pyplot as plt

# Plotting ultiple graphs
plt.axes([x_lo, y_lo, width, height]) # figure units between 0 and 1
plt.subplot()
# before shwoing the figure, issuing tight_layout()
plt.tight_layout(nrows, ncols, nsubplot) # avoid ticklabels and title overlaps
# control axis extents
plt.axis(xmin, xmax, ymin, ymax)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)     # accept either tuple or list
# other options for axis()
plt.axis('off', 'equal', 'square', 'tight')

### Legends, annotations, styles
plt.scatter(x, y, marker='o', color = 'red', label = 'something')
plt.legend(loc='upper right')   #position of legend (9 positions + best + right)
# The position of legend can be given as text or 0-10
# Using annotate() for arrows
plt.annotate(s='text', xy=(...,...), xytext=(...,...), arrowprops={'color':'green'})
# switch styles globally with
plt.style.use() # apply a style to a plot
plt.style.available     # check availibilities

# =============================================================================
# PLOT 2D ARRAYS
# =============================================================================

import numpy as np
# Slicing: slice = start:stop:stride
u = np.linspace(-2, 2, 3)   #create a 1D array for uniformly spaced values
v = np.linspace(-1, 1, 5)   
X,Y = np.meshgrid(u, v)  #replicates the one-dimensional arrays
Z = X**2/25 + Y**2/4
print('Z:\n', Z)
plt.set_cmap('grayscale')   # set the colormap to grayscale
plt.pcolor(Z)   # start from bottem left
plt.show()
# if not set_cmap, the pcolor stands for pseudocolor
plt.pcolor(Z, cmap='gray')   # start from bottem left
plt.colorbar()
plt.axis('tight')   #clear the white space
plt.show()
plt.pcolor(X, Y, Z, cmap='gray')   # start from bottem left

# SMOOTH CURVES: contours
plt.contour(Z, 9)
plt.contourf(Z, 9)  # provide filled contour plot

# Visusulze bivariate distributions
counts, bins, patches = plt.hist(X, bins=25)
# more options for bins in 2d
x = np.linspace(-4, 4, 99)
y = np.linspace(-9, 9, 99)
plt.hist2d(x,y,bins=(44,44))
plt.colorbar()
# hexbin()
plt.hexbin(x, y, gridsize=(15,10))
plt.colorbar()

### working with images
img = plt.imread('....jpg')
print(img.shape)    # return x, y, trailing dimension
plt.imshow(img)
plt.axis('off')
# reduciton to gray_scale image
collapsed = img.mean(axis=2)    #average the RGB channel
plt.set_cmap('gray')
plt.imshow(collapsed, cmap='gray)
# Uneven samples
uneven = collapsed[::4, ::2]
print(uneven.shape)
plt.imshow(uneven, aspect=2.0)  #aspect
plt.imshow(uneven, extent=(0,640,0,480))  #extent to the original size
plt.savefig() #to export the image produced to a file.







