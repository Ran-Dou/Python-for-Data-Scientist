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

### Example
# Import matplotlib.pyplot
import matplotlib.pyplot as plt
# Set the style to 'ggplot'
plt.style.use('ggplot')
# Create a figure with 2x2 subplot layout
plt.subplot(2, 2, 1) 
# Plot the enrollment % of women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')
# Plot the enrollment % of women in Computer Science
plt.subplot(2, 2, 2)
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')
# Add annotation
cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max-1, cs_max-10), arrowprops=dict(facecolor='black'))
# Plot the enrollmment % of women in Health professions
plt.subplot(2, 2, 3)
plt.plot(year, health, color='green')
plt.title('Health Professions')
# Plot the enrollment % of women in Education
plt.subplot(2, 2, 4)
plt.plot(year, education, color='yellow')
plt.title('Education')
# Improve spacing between subplots and display them
plt.tight_layout()
plt.show()

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
plt.hist2d(x,y,bins=(44,44), range=((8,48),(40,235)))
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
plt.imshow(uneven, extent=(0,640,0,480), aspect=1.0)  #extent to the original size
plt.savefig() #to export the image produced to a file.

### Example
# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')
# Extract minimum and maximum values from the image: pmin, pmax
pmin, pmax = image.min(), image.max()
print("The smallest & largest pixel intensities are %d & %d." % (pmin, pmax))
# Rescale the pixels: rescaled_image
rescaled_image = 256*(image - pmin) / (pmax - pmin)
print("The rescaled smallest & largest pixel intensities are %.1f & %.1f." % 
      (rescaled_image.min(), rescaled_image.max()))
# Display the original image in the top subplot
plt.subplot(2,1,1)
plt.title('original image')
plt.axis('off')
plt.imshow(image)
# Display the rescaled image in the bottom subplot
plt.subplot(2,1,2)
plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image)
plt.show()
plt.imshow(uneven, extent=(0,640,0,480))  #extent to the original size
plt.savefig() #to export the image produced to a file.

# =============================================================================
# STATISTICAL PLOTS WITH SEABORNS
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

tips = sns.load_dataset('tips')
# plot groups in different color
sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue='sex', palette='Set1')
# plot groups in different plots
sns.lmplot(x = 'total_bill', y = 'tip', data = tips, col='sex')
# Residual plot
sns.residplot(x='age', y='fare', data=df, color='indianred')
# regplot()
# A principal difference between sns.lmplot() and sns.regplot() is the way in which matplotlib options are passed (sns.regplot() is more permissive).
# For both sns.lmplot() and sns.regplot(), the keyword order is used to control the order of polynomial regression.
# The function sns.regplot() uses the argument scatter=None to prevent plotting the scatter plot points again.
sns.regplot(x='weight', y='mpg', data=auto, color='green', scatter=None, label='order 2', order=2)

### Univariate distribution
# stripplot()
sns.stripplot([x='day'], y='tip', data=tips)
# spread out strip plots
sns.tripplot(x='day', y='tip', data=tips, size=4, jitter=True)
# swarm plot
sns.swarmplot(x='day', y='tip', data=tips)
sns.swarmplot(x='day', y='tip', data=tips, hue='sex')
# interchange x y axis
sns.swarmplot(x='tip', y='day', data=tips, hue='sex', orient='h')
# box plot/ violin plot
sns.boxplot(x='day', y='tip', data=tips)
sns.violinplot(x='day', y='tip', data=tips)
# combine plots
sns.violinplot(x='day', y='tip', data=tips, inner=None, color='lightgray')
sns.stripplot(x='day', y='tip', data=tips, size=4, jitter=True)

### Multivariate distribution
# joint plot
# pearson correlation coefficient quantifies how strongly two variables are correlated
# p-value tells the statistical significance of the difference of this value from 0.
sns.jointplot(x='total_bill', y='tip', data=tips)
# KDE: Kernel density estimation --> result in smooth contour plots and surfaces instead
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
#kind='scatter' uses a scatter plot of the data points
#kind='reg' uses a regression plot (default order 1)
#kind='resid' uses a residual plot
#kind='kde' uses a kernel density estimate of the joint distribution
#kind='hex' uses a hexbin plot of the joint distribution
# pair plots
sns.pairplot(tips)  # only use numerical columns
# heatmap
sns.heatmap(covariance)
































