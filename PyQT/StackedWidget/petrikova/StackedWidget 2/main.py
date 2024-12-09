from PyQt5 import QtWidgets
import sd

ocenka = {
    0 : 2,
    1 : 3,
    2 : 4,
    3 : 5
}

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Form()
        self.ui.setupUi(self)
        self.ui.page_4.setCurrentIndex(0)
        self.ui.GoButton.clicked.connect(self.test1)
        self.ui.dalee1.clicked.connect(self.test2)
        self.ui.dalee2.clicked.connect(self.test3)
        self.ui.dalee1_3.clicked.connect(self.end)
        self.ui.domoy.clicked.connect(self.dom)
        
    def test1(self):
        self.ui.page_4.setCurrentIndex(1)
    
    def test2(self):
        self.ui.page_4.setCurrentIndex(2)
        
    def test3(self):
        self.ui.page_4.setCurrentIndex(3)
    
    def end(self):
        
        score = 0
        self.ui.page_4.setCurrentIndex(4)
        if self.ui.radioButton.isChecked():
            score += 0
        if self.ui.radioButton_2.isChecked():
            score += 0
        if self.ui.radioButton_3.isChecked():
            score += 1
        if self.ui.radioButton_4.isChecked():
            score += 0
        if self.ui.radioButton_5.isChecked():
            score += 0
        if self.ui.radioButton_6.isChecked():
            score += 1
        if self.ui.radioButton_7.isChecked():
            score += 0
        if self.ui.radioButton_8.isChecked():
            score += 0
        if self.ui.radioButton_9.isChecked():
            score += 1
        
        self.ui.ball.setText(f"Баллы:  {str(score)}")
        self.ui.ocenka.setText(f"Оценка:  {str(ocenka[score])}")
        
    def dom(self):
        
        self.ui.page_4.setCurrentIndex(0)
        self.ui.ball.clear()
        self.ui.ocenka.clear()
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)
        self.ui.radioButton_4.setChecked(False)
        self.ui.radioButton_5.setChecked(False)
        self.ui.radioButton_6.setChecked(False)
        self.ui.radioButton_7.setChecked(False)
        self.ui.radioButton_8.setChecked(False)
        self.ui.radioButton_9.setChecked(False)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())