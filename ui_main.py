# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(460, 300)
        MainWindow.setStyleSheet(_fromUtf8("QMainWinodw{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton {\n"
"border: 2px solid #333333;\n"
"border-radius: 6px;\n"
"background-color: #222222;\n"
"background-color: QlinearGradient(x1: 0, y1: 0, x2: 0, y2: 0.67, stop: 0 #444444, stop: 1 #222222);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextBrowser {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel {\n"
"border: 2px solid #333333;\n"
"border-radius: 6px;\n"
"background-color: #222222;\n"
"background-color: QlinearGradient(x1: 0, y1: 0, x2: 0, y2: 0.67, stop: 0 #444444, stop: 1 #222222);\n"
"color: white;\n"
"\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.MIC1 = QtGui.QPushButton(self.centralwidget)
        self.MIC1.setGeometry(QtCore.QRect(363, 5, 91, 20))
        self.MIC1.setStyleSheet(_fromUtf8(""))
        self.MIC1.setObjectName(_fromUtf8("MIC1"))
        self.PCM = PlotWidget(self.centralwidget)
        self.PCM.setGeometry(QtCore.QRect(5, 175, 451, 121))
        self.PCM.setObjectName(_fromUtf8("PCM"))
        self.FFT = PlotWidget(self.centralwidget)
        self.FFT.setGeometry(QtCore.QRect(5, 29, 451, 121))
        self.FFT.setObjectName(_fromUtf8("FFT"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 5, 100, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 152, 100, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.MIC1.setText(_translate("MainWindow", "EXIT", None))
        self.label.setText(_translate("MainWindow", "PCM Data", None))
        self.label_2.setText(_translate("MainWindow", "Frequency Data", None))

from pyqtgraph import PlotWidget
