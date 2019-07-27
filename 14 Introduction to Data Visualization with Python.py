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
plt.axis([xmin, xmax, ymin, ymax])
plt.xlim([xmin, xmax])
plt.ylim([ymin, ymax])     # accept either tuple or list
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














