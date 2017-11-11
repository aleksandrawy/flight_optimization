import qgmap
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtWebEngine
import plotly.plotly as py
import sys

# Create an application
from PyQt5.QtCore import QUrl

app = QtWidgets.QApplication(sys.argv)

# And a window
win = QtWidgets.QWidget()
win.setWindowTitle('QWebView Interactive Demo')

# And give it a layout
layout = QtWidgets.QVBoxLayout()
win.setLayout(layout)

view = QtWebEngineWidgets.QWebEngineView()
# view.setHtml('''
# <html>
#   <head>
#     <style>
#        #map {
#         height: 400px;
#         width: 100%;
#        }
#     </style>
#   </head>
#   <body>
#     <h3>My Google Maps Demo</h3>
#     <div id="map"></div>
#     <script>
#       function initMap() {
#         var uluru = {lat: -25.363, lng: 131.044};
#         var map = new google.maps.Map(document.getElementById('map'), {
#           zoom: 4,
#           center: uluru
#         });
#         var marker = new google.maps.Marker({
#           position: uluru,
#           map: map
#         });
#       }
#     </script>
#     <script async defer
#     src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
#     </script>
#   </body>
# </html>
# ''')


# view.setHtml('''
# <html>
#     <head>
#         <meta charset='utf-8' />
#         <title></title>
#         <script src='https://api.tiles.mapbox.com/mapbox-gl-js/v0.41.0/mapbox-gl.js'></script>
#         <link href='https://api.tiles.mapbox.com/mapbox-gl-js/v0.41.0/mapbox-gl.css' rel='stylesheet' />
#         <style>
#             #map {
#                 height: 400px;
#                 width: 100%;
#             }
#         </style>
#     </head>
#     <body>
#     <h3>My MapBox Demo</h3>
#     <div id='map' style='width: 400px; height: 300px;'></div>
#     <script>
#         mapboxgl.accessToken = 'pk.eyJ1IjoiYWxld3lzemVja2EiLCJhIjoiY2o4dDV5YTNiMGRldzJxcWFmcDZ1MjdtNyJ9.AR35L19M-Pbh57YKcB1ZHg';
#         var map = new mapboxgl.Map({
#             container: 'map',
#             style: 'mapbox://styles/mapbox/dark-v9'
#
#         });
#         map.show()
#
#     </script>
#
#     </body>
# </html>
# ''')

# view.setHtml('''
#   <!DOCTYPE html>
#     <head>
#       <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
#     </head>
#     <body>
#     <!-- Plotly chart will be drawn inside this div -->
#     <div id="plotly-div"></div>
#       <script>
#         trace1 = {
#           lat: ['45.5017'],
#           latsrc: 'alewyszecka:1:fe6604',
#           lon: ['-73.5673'],
#           lonsrc: 'alewyszecka:1:442669',
#           marker: {size: 14},
#           mode: 'markers',
#           text: ['Montreal'],
#           textsrc: 'alewyszecka:1:ed7771',
#           type: 'scattermapbox'
#         };
#         data = [trace1];
#         layout = {
#           autosize: true,
#           hovermode: 'closest',
#           mapbox: {
#             accesstoken: 'pk.eyJ1IjoiYWxld3lzemVja2EiLCJhIjoiY2o4dDV5YTNiMGRldzJxcWFmcDZ1MjdtNyJ9.AR35L19M-Pbh57YKcB1ZHg',
#             bearing: 0,
#             center: {
#               lat: 45,
#               lon: -73
#             },
#             pitch: 0,
#             zoom: 5
#           }
#         };
#         Plotly.plot('plotly-div', {
#           data: data,
#           layout: layout
#         });
#       </script>
#     </body>
#   </html>
#   ''')
url = 'C:/Users/tralala/Desktop/Praca Inżynierska/basic.html'
with open(url) as map:
    data = map.read()
map.closed

print(data)
#####PONIZEJ DZIALA!!!
view.setHtml(data)


button = QtWidgets.QPushButton('Set Full Name')

def complete_name():
    # frame = view.page()
    # print(frame.runJavaScript('completeAndReturnName();'))
    frame = view.setHtml('''
<!DOCTYPE html>
<html>
    <head>
        <meta charset=utf-8 />
        <title>A simple map</title>
        <meta name='viewport' content='initial-scale=1,maximum-scale=1,user-scalable=no' />
        <script src='https://api.mapbox.com/mapbox.js/v3.1.1/mapbox.js'></script>
        <link href='https://api.mapbox.com/mapbox.js/v3.1.1/mapbox.css' rel='stylesheet' />
        <style>
          body { margin:0; padding:0; }
          #map { position:absolute; top:0; bottom:0; width:100%; }
        </style>
    </head>
    <body>
        <div id='map'></div>
        <script>
        L.mapbox.accessToken = 'pk.eyJ1IjoiYWxld3lzemVja2EiLCJhIjoiY2o4dDV5YTNiMGRldzJxcWFmcDZ1MjdtNyJ9.AR35L19M-Pbh57YKcB1ZHg';
        var map = L.mapbox.map('map', 'mapbox.streets')
            .setView([40, -74.50], 9);
        L.tileLayer('https://api.mapbox.com/styles/v1/alewyszecka/cj91ajcq72nv12rs8d761qkov/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYWxld3lzemVja2EiLCJhIjoiY2o4dDV5YTNiMGRldzJxcWFmcDZ1MjdtNyJ9.AR35L19M-Pbh57YKcB1ZHg').addTo(map);
        </script>
    </body>
</html>
''')

   # print(frame.runJavaScript('completeAndReturnName();'))


button.clicked.connect(complete_name)

#view = py.get_figure("https://plot.ly/~alewyszecka/0/")


# w = QtWidgets.QDialog()
# view = qgmap.QGoogleMap(w)
layout.addWidget(view)
layout.addWidget(button)

# Show the window and run the app
win.show()
app.exec_()
