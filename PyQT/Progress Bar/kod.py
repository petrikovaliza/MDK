from PyQt5 import QtWidgets, QtCore
import time
import main_window, zastavka


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
      
class Zastavka(QtWidgets.QWidget):   
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = zastavka.Ui_Zastavka()
        self.ui.setupUi(self)
        self.ui.zagruziButton.clicked.connect(self.doAction)
        
    def doAction(self):
        a = 0
        self.ui.WaitLabel.setText("Ожидайте, пожалуйста...")
        while a < 100:
            a += 10
            time.sleep(0.5)
            self.ui.progressBar.setValue(a)          
        else:
            zastavka.close()
            main.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.setWindowFlag(QtCore.Qt.Drawer)
    zastavka = Zastavka()
    zastavka.setWindowFlag(QtCore.Qt.SplashScreen)
    zastavka.show()
    sys.exit(app.exec_())