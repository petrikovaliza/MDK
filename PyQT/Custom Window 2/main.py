from PyQt5 import QtWidgets
import avtoriz_window, main_window, wrong_window

users = {
    "admin" : "admin",
    "liza" : "12345",
    "kuk" : "lala",
    "Arthur Morgan" : "454545",
}

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main_window.Ui_Main()
        self.ui.setupUi(self)
      
class Wrong(QtWidgets.QWidget):   
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = wrong_window.Ui_Wrong()
        self.ui.setupUi(self)
        self.ui.ok.clicked.connect(self.close_wrong)
        
    def close_wrong(self):
        
        wrong.close()
             
class Avtorization(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = avtoriz_window.Ui_Avtorization()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.open_main)
        self.ui.pushButton_2.clicked.connect(self.close_avtoriz)
        
           
    def open_main(self):
        
        username = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()

        if not username or not password:
            wrong.show()
            wrong.ui.label.setText("Заполните оба поля!")
            return

        if username in users and users[username] == password:
            main.show()
            avtoriz.close()
            main.ui.label.setText(f"Добро пожаловать, {username}")
        else:
            wrong.show()
            wrong.ui.label.setText("Неверный логин или пароль.")
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            
    def close_avtoriz(self):
        
        avtoriz.close()
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    avtoriz = Avtorization()
    wrong = Wrong()
    avtoriz.show()
    sys.exit(app.exec_())