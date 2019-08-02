import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# =============================================================================
# BASIC PLOTTING WITH BOKEH
# =============================================================================

### Glyphs
# visual shapes, with properties attached to data
from bokeh.io import output_file, show
from bokeh.plotting import figure
plot = figure(plot_width=400, tools='pan,box_zoom')
plot.circle([1,2,3,4,5],[8,6,5,2,3])
output_file('circle.html')
show(plot)

plot = figure()
plot.circle(x=10, y=[2,5,8,12], size=[10,20,30,40])

### Markers
# asterisk, circle, circle_cross, circle_x, cross, diamond, diamond_cross
# inverted_triangle, square, square_cross, square_x, triangle, x
### Additional glyphs
# line
x = [1,2,3,4,5]
y = [8,6,5,2,3]
plot = figure()
plot.line(x,y,line_width=3)
plot.circle(x,y,fill_color='white', size=10)
output_file('line.html')
show(plot)
# Patches: data given as 'list of lists'
xs = [[1,1,2,2],[2,2,4],[2,2,3,3]]
ys = [[2,5,5,2],[3,5,5],[2,3,4,2]]
plot = figure()
plot.patches(xs, ys, fill_color=['red','blue','green'], line_color='white')
output_file('patches.html')
show(plot)
# Other glyphs
# annulus, annular_wedge, wedge, rect, quad, vbar, hbar, image, image_rgba, imgae_rul
# patch, patches, line, multi_line, circle, oval, ellipse, arc, quadratic, bezier

### Data Formats
# NumPy Arrays
import numpy as np
x = np.linspace(0, 10, 1000)
y = np.sin(x) + np.random.random(1000) * 0.2
plot = figure()
plot.line(x,y)
show(plot)
# Pandas
import pandas as pd
from bokeh.sampledata.iris import flowers
plot = figure()
plot.circle(flowers['petal_length'],
            flowers['sepal_length'],
            size=10)
show(plot)
# Column Data Source
# can be shared between glyphs to link selections
# extra columns can be used with hover tooltips
from bokeh.models import ColumnDataSource
source = ColumnDataSource(data={
        'x':[1,2,3,4,5],
        'y':[8,6,5,2,3]})
source.data
from bokeh.sampledata.iris import flowers as df
df.head()
# create columndatasource from a dataframe
source = ColumnDataSource(df)

### Customizing glyphs
# Selection appearance
plot = figure(tools='box_select, lasso_select')
petal_length = flowers['petal_length']
sepal_length = flowers['sepal_length']
plot.circle(petal_length, sepal_length,
            selection_color='red',
            nonselection_fill_alpha=0.2,
            nonselection_fill_color='grey')
show(plot)
# Hover appearance
from bokeh.models import HoverTool
hover = HoverTool(tooltips=None, mode='hline')
plot = figure(tools=[hover, 'crosshair'])
plot.circle(petal_length, sepal_length,
            size=15, hover_color='red')
show(plot)
# Color mapping
from bokeh.models import CategoricalColorMapper
mapper = CategoricalColorMapper(factors=['setosa','virginica','versicolor'],
                                palette=['red','green','blue'])
plot = figure(x_axis_label='petal_length',
              y_axis_label='sepal_length')
plot.circle('petal_length', 'sepal_length', size=10, source=flowers,
            color={'field':'species', 'transform':mapper})
show(plot)

##### http://www.colors.commutercreative.com/grid/

# add additional tool to an existing plot
p.add_tools()

# =============================================================================
# LAYOUTS, INTERACTIONS, ANNOTATIONS
# =============================================================================

# arranging multiple plots
from bokeh.layouts import row
layout = row(p1, p2, p3)
output_file('row.html')
show(layout)
from bokeh.layouts import column
layout = column(p1, p2, p3)
output_file('column.html')
show(layout)

# nested layouts
layout = row(column(p1,p2),p3)

### advanced layouts
# gridplots
from bokeh.layouts import gridplot
# give a list of rows for layout
layout = gridplot([[None, p1],[p2, p3]], toolbar_location=None)
output_file('nested.html')
show(layout)
# By using the sizing_mode argument, you can scale the widths to fill the whole figure.

# tabbed layouts
from bokeh.models.widgets import Tabs, Panel
# creat a panel with a title for each tab
first = Panel(child=row(p1,p2), title='first')
second = Panel(child=row(p3), title='second')
# put panels in a tabs object
tabs = Tabs(tabs = [first, second])
output_file('tabbed.html')
show(tabs)

# linking plots together
p3.x_range = p2.x_range = p1.x_range
p3.y_range = p2.y_range = p1.y_range
# linking selection
# share the same data source 'source'
# Legends
plot.circle('petal_length', 'sepal_length', size=10, source=flowers,
            color={'field':'species', 'transform':mapper}, legend='species')
plot.legend.location='top_left'
from bokeh.models import HoverTool
hover = HoverTool(tooltips = [('species name', '@species'),
                              ('petal length', '@petal_length'),
                              ('sepal length', '@sepal_length')])
plot = figure(tools=[hover, 'pan', 'wheel_zoom'])
















