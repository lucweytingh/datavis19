function scrollToElem(elem) {
  elem.scrollIntoView({
    behavior: 'smooth'
  });
}

$section = $('.section').first();

function scrollToSection(direction) {
  if (direction === 1) {
    console.log($section.next());
    if ($section.next().length > 0) {
      $section = $section.next();
    }
  } else {
    if ($section.prev().length > 0) {
      $section = $section.prev();
    }
  }
  scrollToElem($section[0]);
}

$(document).keydown(function(e) {
  switch(e.which) {
    case 37: // left
    console.log("left")
    scrollToSection(-1);
    break;

    case 38: // up
    console.log("up")
    scrollToSection(-1);
    break;

    case 39: // right
    console.log("right")
    scrollToSection(1);
    break;

    case 40: // down
    console.log("down")
    scrollToSection(1);
    break;

    default: return; // exit this handler for other keys
  }
  e.preventDefault(); // prevent the default action (scroll / move caret)
});


var $wrapper = $('#total_rows');
var $header = $wrapper.find('.header');
var $container = $wrapper.find('.chart-container');
var options = {'label_prepend': 'Amount of rows per country', 'library': {'backgroundColor': {'fill': 'transparent'}, 'datalessRegionColor': '#f5f5f5', 'defaultColor': '#f5f5f5'}};

function render_chart(index, data) {
  var $newChart = $('<div id="chart-' + index + '" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0;"></div>')
  $newChart.appendTo($container);

  new Chartkick.GeoChart("chart-" + String(index), data, options);
  setTimeout(function() { $newChart.css("z-index", index); }, 100);
  return $newChart;
}
render_chart(0, [['Afghanistan', 3517], ['Algeria', 1328], ['Armenia', 6406], ['Azerbaijan', 125], ['Bangladesh', 3178], ['Benin', 3452], ['Bhutan', 78], ['Bolivia', 4248], ['Burkina Faso', 9168], ['Burundi', 4054], ['Cambodia', 3203], ['Cameroon', 5078], ['Cape Verde', 276], ['Central African Republic', 2052], ['Chad', 3175], ['Colombia', 8084], ['Congo', 2785], ["Cote d'Ivoire", 4708], ['Democratic Republic of the Congo', 28260], ['Djibouti', 3235], ['Egypt', 1462], ['El Salvador', 6027], ['Ethiopia', 9536], ['Gambia', 22814], ['Georgia', 80], ['Ghana', 8317], ['Guatemala', 3001], ['Guinea', 2828], ['Guinea-Bissau', 1467], ['Haiti', 5403], ['India', 72957], ['Indonesia', 1373], ['Iran  (Islamic Republic of)', 320], ['Iraq', 3356], ['Jordan', 3271], ['Kenya', 3717], ['Kyrgyzstan', 18461], ["Lao People's Democratic Republic", 16968], ['Lebanon', 15707], ['Lesotho', 5475], ['Liberia', 5999], ['Madagascar', 6557], ['Malawi', 15723], ['Mali', 34665], ['Mauritania', 5627], ['Mozambique', 23698], ['Myanmar', 13868], ['Nepal', 4845], ['Niger', 37199], ['Nigeria', 11621], ['Pakistan', 4544], ['Peru', 974], ['Philippines', 18115], ['Rwanda', 110857], ['Senegal', 23553], ['South Sudan', 5254], ['Sri Lanka', 3364], ['State of Palestine', 7234], ['Sudan', 4598], ['Swaziland', 717], ['Syrian Arab Republic', 21654], ['Tajikistan', 19841], ['Timor-Leste', 1440], ['Turkey', 2501], ['Uganda', 3355], ['Ukraine', 27716], ['United Republic of Tanzania', 7634], ['Yemen', 10292], ['Zambia', 27745], ['Zimbabwe', 2683]]);
