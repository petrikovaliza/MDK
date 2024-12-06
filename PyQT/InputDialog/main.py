from PyQt5 import QtWidgets, QtGui, QtCore
import sd

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Wooow()
        self.ui.setupUi(self)
        self.ui.vvod_stroki.clicked.connect(self.Text)
        self.ui.vvod_int.clicked.connect(self.Int)
        self.ui.vvod_float.clicked.connect(self.Double)
        self.ui.choice_punkt.clicked.connect(self.Item)
 
    def Text(self):
        text, ok = QtWidgets.QInputDialog.getText(window,"Ввод строки", "Введите буквы", echo=0)
        if ok:
            self.ui.print.setText(str(text))
        
    def Int(self):
        int_chislo, ok = QtWidgets.QInputDialog.getInt(window, "Ввод целого числа", "Введите число от 0 до 15", min = 0, max = 15, step=1)
        if ok:
            self.ui.print.setText(str(int_chislo))
        
    def Double(self):
        double_chislo, ok = QtWidgets.QInputDialog.getDouble(window, "Ввод вещественного числа", "Введите число от 0 до 10", min = 0, max = 10, decimals=3)
        if ok:
            self.ui.print.setText(str(double_chislo))
            
    def Item(self):
        item, ok = QtWidgets.QInputDialog.getItem(window, "Выбор пункта", "Выберите пункт", ["Кошки", "Собаки", "Лошади"], current=0, editable=False)
        if ok:
            self.ui.print.setText(str(item))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())