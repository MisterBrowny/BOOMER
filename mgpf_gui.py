# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mgpf_gui.ui'
#
# Created: Fri Jul 28 02:16:53 2017
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1018, 758)
        font = QtGui.QFont()
        font.setPointSize(80)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 320, 471, 411))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("font: 72pt \"Sans Serif\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lcd_msec = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_msec.setGeometry(QtCore.QRect(610, 120, 151, 191))
        self.lcd_msec.setNumDigits(3)
        self.lcd_msec.setMode(QtGui.QLCDNumber.Dec)
        self.lcd_msec.setObjectName(_fromUtf8("lcd_msec"))
        self.lcd_seconde = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_seconde.setGeometry(QtCore.QRect(450, 120, 141, 191))
        self.lcd_seconde.setNumDigits(2)
        self.lcd_seconde.setObjectName(_fromUtf8("lcd_seconde"))
        self.lcd_minute = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_minute.setGeometry(QtCore.QRect(290, 120, 141, 191))
        self.lcd_minute.setNumDigits(2)
        self.lcd_minute.setObjectName(_fromUtf8("lcd_minute"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MGPF", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "START", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

