from PyQt5 import QtWidgets, QtCore, QtMultimedia
import sys, os
import sd

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window |
                                   QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Звуковые эффекты")
        
        # Инициализируем подсистему вывода звуковых эффектов
        self.sndEffect = QtMultimedia.QSoundEffect ()
        self.sndEffect.setVolume(0.5)

        # Задаем файл-источник
        fn = QtCore.QUrl.fromLocalFile(os.path.abspath("zvuk-gorbatogo-kita.wav"))
        self.sndEffect.setSource(fn)
        self.sndEffect.loopsRemainingChanged.connect(self.showCount)
        self.sndEffect.playingChanged.connect(self.clearCount)
        vbox = QtWidgets.QVBoxLayout()
        
        # Создаем кнопки для запуска воспроизведения звука
        lblPlay = QtWidgets.QLabel("Воспроизвести...")
        vbox.addWidget(lblPlay)
        btOnce = QtWidgets.QPushButton("...&один раз")
        btOnce.clicked.connect(self.playOnce)
        vbox.addWidget(btOnce)
        btnTen = QtWidgets.QPushButton("...&десять раз")
        btnTen.clicked.connect(self.playTen)
        vbox.addWidget(btnTen)
        btnInfinite = QtWidgets.QPushButton("...&бесконечное количество раз")
        btnInfinite.clicked.connect(self.playInfinite)
        vbox.addWidget(btnInfinite)
        btnStop = QtWidgets.QPushButton("&Стоп")
        btnStop.clicked.connect(self.sndEffect.stop)
        vbox.addWidget(btnStop)
        self.lblStatus = QtWidgets.QLabel("")
        vbox.addWidget(self.lblStatus)
        self.setLayout(vbox)
        self.resize(200, 100)
        
    def playOnce(self):
        self.sndEffect.setLoopCount(1)
        self.sndEffect.play()
    
    def playTen(self):
        self.sndEffect.setLoopCount(10)
        self.sndEffect.play()
    
    def playInfinite(self):
        self.sndEffect.setLoopCount(QtMultimedia.QSoundEffect.Infinite)
        self.sndEffect.play()

    # Выводим количество повторений воспроизведения эффекта  
    def showCount(self):
        self.lblStatus.setText("Воспроизведено " + str(self.sndEffect.loopCount() -
                                                       self.sndEffect.loopsRemaining()) + " раз")
        
     # Если воспроизведение закончено, очищаем выведенное ранее количество повторений эффекта  
    def clearCount(self):
        if not self.sndEffect.isPlaying():
            self.lblStatus.setText("")

   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())   