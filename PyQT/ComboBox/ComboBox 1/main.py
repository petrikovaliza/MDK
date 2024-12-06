from PyQt5 import QtWidgets, QtGui, QtCore
import sd

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Form()
        self.ui.setupUi(self)

        self.ui.comboBox.currentIndexChanged.connect(self.box)
        
        
    def box(self):
        self.ui.label.setText(str(self.ui.comboBox.currentText()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())