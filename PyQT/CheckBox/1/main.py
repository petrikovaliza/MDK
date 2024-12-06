from PyQt5 import QtWidgets
import sd

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.cheker)
        self.ui.pushButton_2.clicked.connect(self.clear)

        
    def cheker(self):
        if self.ui.checkBox.isChecked():
            self.ui.label.setText('Привет')
        
        if self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked():
            self.ui.label_2.setText('Привет Hello')
        
        if self.ui.checkBox.isChecked() and self.ui.checkBox_3.isChecked():
            self.ui.label_3.setText('??')
        
        if self.ui.checkBox_2.isChecked():
            self.ui.label_2.setText('Да')
        
        if self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked():
            self.ui.label_2.setText('Нет')
        
        if self.ui.checkBox_3.isChecked():
            self.ui.label_3.setText('Ого')
        
        if self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked() and self.ui.checkBox_3.isChecked():
            self.ui.label.setText('Wooow!')
            self.ui.label_2.setText('Wooow!')
            self.ui.label_3.setText('Wooow!')
        
    def clear(self):
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_3.setChecked(False)
        self.ui.label.clear()
        self.ui.label_2.clear()
        self.ui.label_3.clear()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())