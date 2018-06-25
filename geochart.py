import os
import webbrowser

import imgkit

from helpers import *

def plot_geochart(name, data, options = {}):
  f = open("charts/{0}.html".format(name),'w')

  options.update({
    'library': {
      'datalessRegionColor': '#f5f5f5',
      'defaultColor': '#f5f5f5'
    }
  })

  content = """<html>
  <head>
    <script src="https://www.gstatic.com/charts/loader.js"></script>
    <script src="../chartkick.js"></script>
  </head>
  <body>
    <div id="{0}" style="width: 80%; height: auto; min-width: 1000px"></div>

    <script>
      new Chartkick.GeoChart("{0}", {1}, {2})
    </script>
  </body>
  </html>""".format(name, data, options)

  f.write(content)
  f.close()

  filename = os.path.abspath(os.path.dirname(__file__)) + "/charts/" + name + ".html"
  webbrowser.open_new_tab("file://" + filename)
  return filename


def html_to_png(filename, name):
  options = {
    'format': 'png',
    'encoding': "UTF-8"
  }
  create_dir('charts/gif')
  imgkit.from_file(filename, 'charts/gif/' + name, options)
