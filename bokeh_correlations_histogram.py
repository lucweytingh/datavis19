from init import *
import scipy.special

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

corr_data = init_json('data/correlations.txt')

corrs = [c['correlation'] for c in corr_data]

p1 = figure(title="Distributie van correlatie-coëfficiënten (r) tussen producten",tools="save",plot_width=1000, plot_height=600)

hist, edges = np.histogram(corrs, density=False, bins=200)

x = np.linspace(-1, 1, 1000)

p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:])

p1.legend.location = "center_right"
p1.legend.background_fill_color = "darkgrey"
p1.xaxis.axis_label = 'r'
p1.yaxis.axis_label = 'Aantal correlaties'

show(p1)
