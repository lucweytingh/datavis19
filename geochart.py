import os
import webbrowser

#import imgkit

from helpers import *

def plot_geochart(name, data, options = {}):
  f = open("charts/{0}.html".format(name),'w')

  dynamic_data = len(data[0]) > 2
  labels = options["labels"] if "labels" in options.keys() else []
  label_prepend = options["label_prepend"] if "label_prepend" in options.keys() else ""
  framerate = options["framerate"] if "framerate" in options.keys() else 2

  options.update({
    'library': {
      'datalessRegionColor': '#f5f5f5',
      'defaultColor': '#f5f5f5'
    }
  })

  if dynamic_data:
    initial_data = data[0]
    dynamic_js = """
      $(function() {{
        $play = $('<div class="play" style="text-align: center; width: 30px; height: 30px; border-radius: 3px; border: 1px solid #ccc">Play</div>');
        $play.appendTo('body');
        var framerate = {1};
        var interval = 1000 / framerate;

        var states = {0};
        var index = 1;

        var intervalObj;
        var playing = false;

        var labels = {2};
        var labelPrepend = "{3}";
        if (labels.length > 0) {{
          $label = $('<h3>' + labelPrepend + labels[0] + '</h3>');
          $label.prependTo('body');
        }}

        function update_label(index) {{
          if (labels.length > 0) {{
            $label.text(labelPrepend + String(labels[index % labels.length]));
          }}
        }}

        function update_data() {{
          var state = states[index % states.length];
          chart.updateData(state);
          update_label(index);
          index++;
        }}

        $play.click(function() {{
          if (playing) {{
            clearInterval(intervalObj);
            $play.text("Play");
            playing = false;
          }} else {{
            intervalObj = setInterval(update_data, interval);
            $play.text("Pause");
            playing = true;
          }}
        }});
      }});
    """.format(data, framerate, labels, label_prepend)
  else:
    initial_data = data
    dynamic_js = ""

  content = """<html>
  <head>
    <script src="https://www.gstatic.com/charts/loader.js"></script>
    <script src="../chartkick.js"></script>


    <script
    src="https://code.jquery.com/jquery-3.3.1.min.js"
    integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
    crossorigin="anonymous"></script>
  </head>
  <body>
    <div id="{0}" style="width: 80%; height: auto; min-width: 1000px"></div>

    <script>
      var chart = new Chartkick.GeoChart("{0}", {1}, {2});

      {3}
    </script>
  </body>
  </html>""".format(name, initial_data, options, dynamic_js)

  f.write(content)
  f.close()

  filename = os.path.abspath(os.path.dirname(__file__)) + "/charts/" + name + ".html"
  webbrowser.open_new_tab("file://" + filename)
  return filename


# def html_to_png(filename, name):
#   options = {
#     'format': 'png',
#     'encoding': "UTF-8"
#   }
#   create_dir('charts/gif')
#   imgkit.from_file(filename, 'charts/gif/' + name, options)
