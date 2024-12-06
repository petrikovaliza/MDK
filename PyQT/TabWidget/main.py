from PyQt5 import QtWidgets
import sd

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Form()
        self.ui.setupUi(self)
        self.ui.calcAmort.clicked.connect(self.amort)
        self.ui.clickAdd.clicked.connect(self.card)

    def amort(self):
        a = float(self.ui.enterPrice.text())
        b = float(self.ui.enterNorma.text())
        c = a * b
        self.ui.print_amort.setText(f"Амортизация налогового учета - {c}")
    
    def card(self):
        d = int(self.ui.enterNumberCard.text())
        e = (self.ui.enterName.text())
        f = (self.ui.enterData.text())
        g = int(self.ui.EnterBackNumber.text())
        self.ui.baza.setText(f"NumberCard - {d}\nOwnerName - {e}\nValidUntil - {f}\nBackDigits - {g}")

                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())