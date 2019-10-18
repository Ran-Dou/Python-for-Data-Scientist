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
# By using the sizing_mode argument, you can scale the widths to fill the whole figure.
row2 = row([mpg_hp, mpg_weight], sizing_mode='scale_width')

### advanced layouts
# gridplots
from bokeh.layouts import gridplot
# give a list of rows for layout
layout = gridplot([[None, p1],[p2, p3]], toolbar_location=None)
output_file('nested.html')
show(layout)

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
p.add_tools(hover)

# =============================================================================
# BUILD INTERACTIVE APPS WITH BOKEH
# =============================================================================

# Basic app outline
from bokeh.io import curdoc
# create plots and widgets
# add callbacks
# arrange plots and widgets in layouts
curdoc.add_root(layout)

# Run bokeh applications
# Run single module apps at the shell or Windows command prompt:
bokeh serve --show myapp.py
# directory style apps run similarly
bokeh serve --show myappdir/
# or 
bokeh serve script.py

### Connecting sliders to plots
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column
from numpy.random import random
N = 300
source = ColumnDataSource(data = {'x':random(N), 'y':random(N)})
plot = figure()
plot.circle('x', 'y', source = source)
slider = Slider(start=100, end=1000, value=N, step=10, title='Number of points')
# add call back to widgets
# bokeh callback can be added to any property
def callbak(attr, old, new):
    # attribute want to change, old/new value
    # don't have to change the name of the arguments
    N = slider.value
    source.data = {'x':random(N), 'y':random(N)}
# change the slider using callback
slider.on_change('value', callback)
# arrange plots and widgets in layouts
layout = column(slider, plot)
# add the layout and all the contains to the current document
curdoc().add_root(layout)

### Updating plots from dropdowns
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column
from numpy.random import random, normal, lognormal
N = 1000
source = ColumnDataSource(data={'x':random(N), 'y':random(N)})
plot = figure()
plot.circle('x', 'y', source=source)
menu = Select(options=['uniform', 'normal', 'lognormal'], value='uniform', title='Distribution')
def callback(attr, old, new):
    if menu.value == 'uniform': f = random
    if menu.value == 'normal': f = normal
    else: f = lognormal
    source.data = {'x':f(size=N), 'y':f(size=N)}
menu.on_change('value', callback)
layout = column(menu, plot)
curdoc.add_root(layout)

### Buttons
from bokeh.models import Button
button = Button(label='press me')
def update():
    # do something interesting
button.on_click(update)
# other button options
from bokeh.models import CheckboxGroup, RadioGroup, Toggle
toggle = Toggle(label='Some on/off', button_type='success')
checkbox = CheckboxGroup(labels=['foo','bar','baz'])
radio = RadioGroup(labels=['2000', '2010'. '2020'])
curdoc().add_root(widgetbox(toggle, checkbox, radio))
def callback(active):
    # Active tells which button is active

### hosting applications for wider audiences

### Exercises
from bokeh.io import curdoc
from bokeh.plotting import figure
plot = figure()
plot.line(x=[1,2,3,4,5], y=[2,5,4,6,7])
curdoc().add_root(plot)










