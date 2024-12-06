from PyQt5 import QtWidgets
import sd

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.calculate_button.clicked.connect(self.perimetr)
        self.ui.clear_button.clicked.connect(self.clear)
        
    def perimetr(self):
        a = float(self.ui.input_a.text())
        b = float(self.ui.input_b.text())
        c = 2 * (a + b)
        self.ui.Perimetr_answer.setText(f"Периметр = {str(c)}")
        
    def clear(self):
        self.ui.input_a.clear()
        self.ui.input_b.clear()
        self.ui.Perimetr_answer.setText(f"Периметр = ")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())