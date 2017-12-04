import json
from collections import OrderedDict
from PyQt5 import QtWebKitWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlanningWindow(object):

    def __init__(self):
        self.view = QtWebKitWidgets.QWebEngineView()

    def openPlanningWindow(self):
        self.PlanningWindow = QtWidgets.QDialog()
        self.PlanningWindow.setWindowTitle('Flight optimization')
        # self.view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.WebGLEnabled, True)
        # self.view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.JavascriptEnabled, True)
        # self.view.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.Accelerated2dCanvasEnabled, True)
        self.setupUi(self.PlanningWindow)
        self.PlanningWindow.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Planning")
        Dialog.resize(800, 600)
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

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 150, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet(label_stylesheet)

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(100, 230, 220, 22))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_c = QtWidgets.QComboBox(Dialog)
        self.comboBox_c.setGeometry(QtCore.QRect(100, 190, 220, 22))
        self.comboBox_c.setObjectName("comboBox")
        self.comboBox_c.accessibleName()

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(470, 150, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(label_stylesheet)

        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(470, 230, 220, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        self.comboBox_2_c = QtWidgets.QComboBox(Dialog)
        self.comboBox_2_c.setGeometry(QtCore.QRect(470, 190, 220, 22))
        self.comboBox_2_c.setObjectName("comboBox")
        self.comboBox_2_c.accessibleName()

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(125, 20, 550, 110))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet(title_stylesheet)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 300, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet(label_stylesheet)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(100, 480, 220, 22))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 440, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet(label_stylesheet)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(470, 260, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet(label_stylesheet)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(470, 350, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet(label_stylesheet)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(470, 300, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet(text_stylesheet)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(470, 390, 220, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet(text_stylesheet)
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(100, 340, 220, 22))
        self.comboBox_3.setObjectName("comboBox_3")


        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 440, 220, 81))
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
        self.comboBox_3.activated.connect(self.set_mtow)

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

    def set_mtow(self):
        for item in self.planes:
            if item["name"] == self.comboBox_3.currentText():
                self.label_8.setText("  " + item["mtow"] + " kg")

    def set_fuel(self):
        for item in self.planes:
            if item["name"] == self.comboBox_3.currentText():
                self.label_9.setText("  " + item["fuel"] + " ")

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
