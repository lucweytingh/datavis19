from init import *
import scipy.special

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

corr_data = init_json('data/correlations_usd.txt')

item_correlations = {}

for c in corr_data:
  items = (c['item1'], c['item2'])
  set_default(item_correlations, items, [])
  if abs(c['correlation']) < 1:
    item_correlations[items].append(c['correlation'])

items_data = []


for items, corrs in item_correlations.items():
  corrs_sum = sum(corrs)
  corrs_avg = corrs_sum / len(corrs)
  items_data.append([items, corrs_sum, corrs_avg])

corrs = [c[2] for c in items_data]

p1 = figure(title="Distributie van de gemiddelde correlatie-coëfficiënt r tussen twee producten",tools="save", sizing_mode='stretch_both')

hist, edges = np.histogram(corrs, density=False, bins=200)

x = np.linspace(-1, 1, 1000)

p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:])

p1.legend.location = "center_right"
p1.legend.background_fill_color = "darkgrey"
p1.xaxis.axis_label = 'r'
p1.yaxis.axis_label = 'Aantal correlaties'

show(p1)
