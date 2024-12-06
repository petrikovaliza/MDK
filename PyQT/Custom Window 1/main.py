from PyQt5 import QtWidgets
import win_1, win_2

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = win_1.Ui_Form()
        self.ui.setupUi(self)
        self.ui.dalee.clicked.connect(self.open)

    def open(self):
        vt.show()

class Window2(QtWidgets.QWidget):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = win_2.Ui_Form()
        self.ui.setupUi(self)
        self.ui.vvesti.clicked.connect(self.print)
    
    def print(self):
        a = float(self.ui.lineEdit.text())
        window.ui.label.setText(str((a*0.15)))
    
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    vt = Window2()
    window.show()
    sys.exit(app.exec_())