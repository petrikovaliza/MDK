from PyQt5 import QtWidgets
import sqlite3
import Avtoriz, Main, Regis, WrongW

class Avtorization(QtWidgets.QWidget):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Avtoriz.Ui_Avtorization()
        self.ui.setupUi(self)
        self.ui.enterBtn.clicked.connect(self.avto)
        self.ui.regBtn.clicked.connect(self.reg_form)
    
    def reg_form(self):
        avto.close()
        reg.show()      
        
    def avto(self):
        
        login = self.ui.login_text.text().strip()
        passw = self.ui.password_text.text().strip()

        if not login or not passw:
            wrong.show()
            wrong.ui.wrong_label.setText("Заполните оба поля!")
            return
    
        db = sqlite3.connect("magaz.db")
        cursor = db.cursor()
        cursor.execute(f'SELECT name, last_name FROM users WHERE login = "{login}" and password = "{passw}"')
        result = cursor.fetchone()
        
        if result is None:
            wrong.show()
            wrong.ui.wrong_label.setText("Неверные данные")
        else:
            avto.close()
            main.show()
            main.ui.name_label.setText(str(result[0]))
            main.ui.name_label_2.setText(str(result[1]))

class Registration(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Regis.Ui_Registration()
        self.ui.setupUi(self)
        self.ui.zaregBtn.clicked.connect(self.zareg)
        self.ui.cancelBtn.clicked.connect(self.cancel)
        
    def zareg(self):
        
        db = sqlite3.connect("magaz.db")
        cursor = db.cursor()
        
        name = self.ui.name_text.text().strip()
        last_name = self.ui.lastname_next.text().strip()
        login = self.ui.login_textReg.text().strip()
        password = self.ui.password_textReg.text().strip()
        
        if not all([name, last_name, login, password]):
            wrong.show()
            wrong.ui.wrong_label.setText("Заполните все поля!")
            return
        
        db = sqlite3.connect("magaz.db")
        cursor = db.cursor()
        row = (name, last_name, login, password)
        command = "INSERT INTO users (name, last_name, login, password) VALUES (?, ?, ?, ?)"
        cursor.execute(command, row)
        
        db.commit()
        
        wrong.show()
        wrong.ui.wrong_label.setText("Вы успешно зарегистрировались!")
        
        reg.close()
        avto.close()  
        
    def cancel(self):
        reg.close()
        avto.show()
    
class Wrong(QtWidgets.QWidget):   
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = WrongW.Ui_WrongWindow()
        self.ui.setupUi(self)
        self.ui.okBtn.clicked.connect(self.close_wrong)
        
    def close_wrong(self):
        
        wrong.close()
        
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Main.Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    avto = Avtorization()
    avto.show()
    reg = Registration()
    main = MainWindow()
    wrong = Wrong()
    sys.exit(app.exec_())