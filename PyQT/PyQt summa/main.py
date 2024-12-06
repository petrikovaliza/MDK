from PyQt5 import QtWidgets
import sd

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.sum)
        self.ui.pushButton_2.clicked.connect(self.clear)
        
    def sum(self):
        a = float(self.ui.lineEdit.text())
        b = float(self.ui.lineEdit_2.text())
        c = a + b
        self.ui.label_2.setText(f"Сумма = {str(c)}")
        
    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.label_2.setText(f"Сумма = ")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())