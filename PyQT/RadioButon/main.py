from PyQt5 import QtWidgets, QtGui, QtCore
import sd

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Form()
        self.ui.setupUi(self)

        self.ui.perevesti.clicked.connect(self.conver)
        self.ui.Input1.setValidator(QtGui.QDoubleValidator())
        self.ui.Input1.setValidator(
            QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+[.][0-9]")))
        
        self.ui.input2.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("")))
        
    def conver(self):
        c = 0
        a = float(self.ui.Input1.text())
        if self.ui.radioButtonCM1.isChecked() and self.ui.radioButtonCM1.isChecked():
            c = a
        if self.ui.radioButtonCM1.isChecked() and self.ui.radioButtonM2.isChecked():
            c = round(a / 1000, 2)
        if self.ui.radioButtonCM1.isChecked() and self.ui.radioButtonKM2.isChecked():
            c = round(a / 100000, 3)
        if self.ui.radioButtonM1.isChecked() and self.ui.radioButtonCM2.isChecked():
            c = round(a * 100, 3)
        if self.ui.radioButtonM1.isChecked() and self.ui.radioButtonM2.isChecked():
            c = a
        if self.ui.radioButtonM1.isChecked() and self.ui.radioButtonKM2.isChecked():
            c = round(a / 1000, 3)
        if self.ui.radioButtonKM1.isChecked() and self.ui.radioButtonCM2.isChecked():
            c = round(a * 100000, 3)
        if self.ui.radioButtonKM1.isChecked() and self.ui.radioButtonM2.isChecked():
            c = round(a * 1000, 3)
        if self.ui.radioButtonKM1.isChecked() and self.ui.radioButtonKM2.isChecked():
            c = a
        self.ui.input2.setText(str(c))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())