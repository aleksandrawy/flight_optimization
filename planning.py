import json
from collections import OrderedDict
from PyQt5 import QtWebKitWidgets, QtWebKit, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp
from qroundprogressbar import QRoundProgressBar
import time

from dijkstra import Dijkstra


class Ui_PlanningWindow(object):

    def __init__(self):
        self.view = QtWebKitWidgets.QWebView()

    def openPlanningWindow(self):
        self.n = True
        self.PlanningWindow = QtWidgets.QDialog()
        self.PlanningWindow.setWindowTitle('Flight optimization')
        # self.view.settings().setAttribute(QtWebKit.QWebSettings.WebGLEnabled, True)
        # self.view.settings().setAttribute(QtWebKit.QWebSettings.JavascriptEnabled, True)
        # self.view.settings().setAttribute(QtWebKit.QWebSettings.Accelerated2dCanvasEnabled, True)
        self.setupUi(self.PlanningWindow)
        self.PlanningWindow.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Planning")
        Dialog.resize(975, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 31, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 62, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        Dialog.setPalette(palette)

        title_stylesheet = "background-color: #1b1b1b; color: #fafafa"
        text_stylesheet = "background-color: #1b1b1b; color: #fafafa"
        label_stylesheet = "border-style: dotted; border-color: #fafafa; border-width: 2px; color: #fafafa"

        self.progress = QRoundProgressBar(Dialog)
        self.progress.setVisible(False)
        self.progress.setGeometry(QtCore.QRect(840, 460, 100, 100))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 150, 300, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet(label_stylesheet)

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 230, 300, 22))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_c = QtWidgets.QComboBox(Dialog)
        self.comboBox_c.setGeometry(QtCore.QRect(150, 190, 300, 22))
        self.comboBox_c.setObjectName("comboBox")
        self.comboBox_c.accessibleName()

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(520, 150, 300, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(label_stylesheet)

        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(520, 230, 300, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        self.comboBox_2_c = QtWidgets.QComboBox(Dialog)
        self.comboBox_2_c.setGeometry(QtCore.QRect(520, 190, 300, 22))
        self.comboBox_2_c.setObjectName("comboBox")
        self.comboBox_2_c.accessibleName()

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(185, 20, 600, 110))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet(title_stylesheet)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 300, 300, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet(label_stylesheet)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(150, 480, 300, 22))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 440, 300, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet(label_stylesheet)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(520, 260, 300, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet(label_stylesheet)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(520, 350, 300, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet(label_stylesheet)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(520, 300, 300, 31))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet(text_stylesheet)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(520, 390, 300, 31))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet(text_stylesheet)
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 340, 300, 22))
        self.comboBox_3.setObjectName("comboBox_3")


        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 440, 300, 81))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(text_stylesheet)

        with open("eurocontrol.json", encoding='utf-8') as input_file:
            self.data = json.load(input_file)

        countries = OrderedDict()
        for item in self.data:
            country = item["country"]
            if country not in countries:
                countries[country] = item

        self.comboBox_c.addItem("Set country...")
        self.comboBox_c.addItems(sorted(countries))
        self.comboBox_c.activated.connect(self.get_departure_airports)

        self.comboBox_2_c.addItem("Set country...")
        self.comboBox_2_c.addItems(sorted(countries))
        self.comboBox_2_c.activated.connect(self.get_arrival_airports)

        with open("planes.json", encoding='utf-8') as input_file:
            self.planes = json.load(input_file)

        planes = OrderedDict()
        for item in self.planes:
            plane = item["name"]
            planes[plane] = item

        self.comboBox_3.addItem("Set type of airplane...")
        self.comboBox_3.addItems(sorted(planes))
        self.comboBox_3.activated.connect(self.get_info)

        self.pushButton.clicked.connect(self.load_graph)

        self.task = TaskThread()
        self.task.taskFinished.connect(self.onFinished)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def get_departure_airports(self):
        airports = []
        for item in self.data:
            if item["country"] == self.comboBox_c.currentText():
                airports.append(item["name"])
        self.comboBox.clear()
        self.comboBox.addItem("Set airport name...")
        self.comboBox.addItems(sorted(airports))

    def get_arrival_airports(self):
        airports = []
        for item in self.data:
            if item["country"] == self.comboBox_2_c.currentText() and item["name"] != self.comboBox.currentText():
                airports.append(item["name"])
        self.comboBox_2.clear()
        self.comboBox_2.addItem("Set airport name...")
        self.comboBox_2.addItems(sorted(airports))

    def get_info(self):
        self.set_fuel()
        self.set_mtow()

    def set_mtow(self):
        for item in self.planes:
            if item["name"] == self.comboBox_3.currentText():
                self.label_8.setText("  " + item["mtow"] + " kg")

    def set_fuel(self):
        for item in self.planes:
            if item["name"] == self.comboBox_3.currentText():
                self.label_9.setText("  " + item["fuel consumption"] + " lbs")

    def load_graph(self):
        self.progress.setVisible(True)
        self.progress.setBarStyle(QRoundProgressBar.BarStyle.DONUT)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor('#1b1b1b'))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(50, 50, 50))

        self.progress.setPalette(palette)
        self.task.start()
        # n = True
        self.loading = True
        while (self.loading):
            for i in range(0, 100, 1):
                if(not self.loading):
                    break
                self.progress.setValue(i)
                qApp.processEvents()
                time.sleep(0.1)

    def onFinished(self):
        self.loading = False
        self.progress.setVisible(False)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Departure airport"))
        self.label_2.setText(_translate("Dialog", "Arrival airport"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600;\">Flight plan</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "Airplane model"))
        self.label_5.setText(_translate("Dialog", "Time and date of flight"))
        self.label_6.setText(_translate("Dialog", "Maximum Take Off Mass"))
        self.label_7.setText(_translate("Dialog", "Fuel consumption"))
        #self.label_8.setText(_translate("Dialog", "mtow"))
        #self.label_9.setText(_translate("Dialog", "fuel"))
        self.pushButton.setText(_translate("Dialog", "Start planning"))


class TaskThread(QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()

    def run(self):
        dij = Dijkstra()
        city_data = dij.get_city_data()
        city_from = 'Gdańsk Lech Wałęsa Airport'
        city_to = 'John Paul II International Airport Kraków-Balice Airport'
        print(dij.dijkstra(city_from, city_to, city_data, False))
        self.taskFinished.emit()