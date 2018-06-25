import os
import webbrowser

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
    <div id="{0}" style="width: 100%; height: auto"></div>

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
  import GrabzItClient
  from GrabzIt import GrabzItImageOptions

  # Create the GrabzItClient class
  # Replace "APPLICATION KEY", "APPLICATION SECRET" with the values from your account!
  grabzIt = GrabzItClient.GrabzItClient("ZjMyZjM5ZDFiOGUxNGE5ZGI5ZGIxN2YwOGE4NWM3MzQ=", "dj9PPz8/Pz9LPz8AGGwncz8/Sj5IG2VjPyw/Uj8pPz8=")

  options = GrabzItImageOptions.GrabzItImageOptions()
  options.format = "png"

  GrabzIt.FileToImage(filename, options)
  # Then call the Save or SaveTo method

  filepath = os.path.abspath(os.path.dirname(__file__)) + "/charts/gif/" + name + ".jpg"
  grabzIt.SaveTo(filepath) 