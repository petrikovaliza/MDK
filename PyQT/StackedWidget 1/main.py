from PyQt5 import QtWidgets
import sd

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Form()
        self.ui.setupUi(self)
        self.ui.nazadButton.clicked.connect(self.page1)
        self.ui.vperedButton.clicked.connect(self.page2)
 
    def page2(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        
    def page1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())