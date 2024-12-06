from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sd

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sd.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.exit.triggered.connect(app.quit)
        self.ui.about_program.triggered.connect(self.aboutProgramm)
        self.ui.actionOpen.triggered.connect(self.open_file)
        

    def aboutProgramm(self):
        self.ui.aboutProgramLabel.setText("ИП-24-26\nПетрикова")
        
    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All files (*);;Text Files (*.txt)", options=options)
        if file_name.endswith('.txt'):
            with open(file_name, "r", encoding='utf-8') as file:
                content = file.read()
                self.ui.opentxt.setPlainText(content)
        else:
            QtWidgets.QMessageBox.information(window, 'Внимание', 'Можно открыть только txt файл!', 
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())