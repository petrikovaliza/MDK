from PyQt5 import QtWidgets
import sys
import sd

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_Form()
        self.ui.setupUi(self)

        self.ui.clear.clicked.connect(self.clear)
        self.ui.calculate.clicked.connect(self.calculate)

        
    def calculate(self):
        a = self.ui.input_shirina.text()
        h = self.ui.input_vusota.text()
        if len(a) == 0 or len(h) == 0:
            w = QtWidgets.QMessageBox.information(
                self, 'Внимание', 'Введите оба значения',
                buttons=QtWidgets.QMessageBox.Ok,
                defaultButton=QtWidgets.QMessageBox.Ok
            )
        else:
            try:
                a = float(a)
                h = float(h)
                c = a * h

                if not any([self.ui.checkBoxx3.isChecked(), self.ui.checkBoxPlus100.isChecked(),
                            self.ui.checkBox_2.isChecked()]):
                    self.ui.plojadRavna.setText(f"Площадь = {c}")

                if self.ui.checkBoxx3.isChecked():
                    self.ui.plojadRavna.setText(f"Площадь = {c * 3}")

                if self.ui.checkBoxPlus100.isChecked():
                    self.ui.plojadRavna.setText(f"Площадь = {c + 100}")

                if self.ui.checkBox_2.isChecked():
                    self.ui.plojadRavna.setText(f"Площадь = {c / 100}")

                if self.ui.checkBoxx3.isChecked() and self.ui.checkBoxPlus100.isChecked():
                    self.ui.plojadRavna.setText(f"Площадь = {c * 3 + 100}")

                if self.ui.checkBoxx3.isChecked() and self.ui.checkBox_2.isChecked():
                    self.ui.plojadRavna.setText(f"Площадь = {c * 3 / 100}")

                if self.ui.checkBoxPlus100.isChecked() and self.ui.checkBox_2.isChecked():
                    self.ui.plojadRavna.setText(f"Площадь = {(c + 100) / 100}")

                if self.ui.checkBoxx3.isChecked() and self.ui.checkBox_2.isChecked() and self.ui.checkBoxPlus100.isChecked():
                    self.ui.plojadRavna.setText(f"Площадь = {c * 3 / 100 + 100}")

            except ValueError :
                QtWidgets.QMessageBox.warning(
                    self, 'Ошибка', 'Пожалуйста, введите числовые значения.',
                    buttons=QtWidgets.QMessageBox.Ok,
                    defaultButton=QtWidgets.QMessageBox.Ok
                )

    def clear(self):
        self.ui.checkBoxx3.setChecked(False)
        self.ui.checkBoxPlus100.setChecked(False)
        self.ui.checkBox_2.setChecked(False)
        self.ui.input_shirina.clear()
        self.ui.input_vusota.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())