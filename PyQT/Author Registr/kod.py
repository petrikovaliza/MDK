from PyQt5 import QtWidgets
import sqlite3
import Avtoriz_ui, Main_ui, Regis_ui

class Avtorization(QtWidgets.QWidget):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Avtoriz_ui.Ui_Avtorization()
        self.ui.setupUi(self)
        self.regBtn.clicked.connect(self.reg_form)
        self.enterBtn.clicked.connect(self.auto)
    
    def reg_form(self):
        avto.close()
        reg.show()      
        
    def avto(self):
        
        login = self.ui.login_text.text()
        passw = self.ui.password_text.text()
        
        db = sqlite3.connect("magaz.db")
        cursor = db.cursor()
        cursor.execute(f'SELECT name, last_name FROM users WHERE login = "{login}" and password = "{passw}"')
        result = cursor.fetchone()
        
        if result is None:
            QtWidgets.QMessageBox.about(None, "Оповещение", "Неверные данные")
        else:
            avto.close()
            main.show()
            main.ui.name_label.setText(str(result[0]))
            main.ui.name_label_2.setText(str(result[1]))

class Registration(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Regis_ui.Ui_Registration()
        self.ui.setupUi(self)
        self.ui.zaregBtn.clicked.connect(self.zareg)
        self.ui.cancelBtn.clicked.connect(self.cancel)
        
    def zareg(self):
        
        db = sqlite3.connect("magaz.db")
        cursor = db.cursor()
        
        name = self.ui.name_text.text()
        last_name = self.ui.lastname_text.text()
        login = self.ui.login_textReg.text()
        password = self.ui.password_textReg.text()
        
        row = (name, last_name, login, password)
        command = "INSERT INTO users (name, last_name, login2, password) VALUES (?, ?, ?, ?)"
        cursor.execute(command, row)
        
        db.commit()
        
        QtWidgets.QMessageBox.information(None, "Регистрация", "Вы успешно зарегистрировались",
                                          buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        
        reg.close()
        avto.close()
        
    def cancel(self):
        reg.close()
        avto.show()
        
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Main_ui.Ui_Main()
        self.ui.setupUi(self)
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    avto = Avtorization()
    avto.show()
    reg = Registration()
    main = Main()
    sys.exit(app.exec_())