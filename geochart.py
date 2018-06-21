import os
import webbrowser

def plot_geochart(name, data):
  f = open("charts/{0}.html".format(name),'w')

  content = """<html>
  <head>
    <script src="https://www.gstatic.com/charts/loader.js"></script>
    <script src="../chartkick.js"></script>
  </head>
  <body>
    <div id="{0}" style="width: 100%; height: auto"></div>

    <script>
      new Chartkick.GeoChart("{0}", {1})
    </script>
  </body>
  </html>""".format(name, data)

  f.write(content)
  f.close()

  filename = "file://" + os.path.abspath(os.path.dirname(__file__)) + "/charts/" + name + ".html"
  webbrowser.open_new_tab(filename)
