from PyQt5 import QtWidgets
import sd

d = {}
d[0] = 'руб'
d[1] = 'доллар'
d[2] = 'евро'

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Form()
        self.ui.setupUi(self)

        self.ui.comboBox.currentIndexChanged.connect(self.conver)
        self.ui.pushButton.clicked.connect(self.conver)
        
        
    def conver(self):
        c = 0
        a = float(self.ui.lineEdit.text())
        if self.ui.comboBox.currentIndex() == 0 and self.ui.comboBox_2.currentIndex() == 0:
            c = a

        if self.ui.comboBox.currentIndex() == 0 and self.ui.comboBox_2.currentIndex() == 1:
            c = a / 104

        if self.ui.comboBox.currentIndex() == 0 and self.ui.comboBox_2.currentIndex() == 2:
            c = a / 108 

        if self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 0:
            c = a * 104 

        if self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 1:
            c = a 

        if self.ui.comboBox.currentIndex() == 1 and self.ui.comboBox_2.currentIndex() == 2:
            c = a * 0.96

        if self.ui.comboBox.currentIndex() == 2 and self.ui.comboBox_2.currentIndex() == 0:
            c = a * 108 

        if self.ui.comboBox.currentIndex() == 2 and self.ui.comboBox_2.currentIndex() == 1:
            c = a / 0.96

        if self.ui.comboBox.currentIndex() == 2 and self.ui.comboBox_2.currentIndex() == 2:
            c = a   

        self.ui.lineEdit_2.setText(str(c))  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())