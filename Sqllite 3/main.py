import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
import sys
from qtconsole.qtconsoleapp import QtCore


class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("note.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.save_Button.clicked.connect(self.saveChanges)
        self.add_button.clicked.connect(self.addNewTask)
       
    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected:", dateSelected)
        self.updateTaskList(dateSelected)
        
    def updateTaskList(self,date):
        self.taskListWidget.clear()
        
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        
        query = "SELECT task, completed FROM tasks WHERE data = ?"
        row = (date,)
        results = cursor.execute(query,row).fetchall()
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags()| QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.taskListWidget.addItem(item)
            
    def saveChanges(self):
        db = sqlite3.connect('data.db')
        cursor = db.cursor()
        data = self.calendarWidget.selectedDate().toPyDate()
        
        for i in range(self.taskListWidget.count()):
            item = self.taskListWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND data = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND data = ?"
            row = (task, data,)
            cursor.execute(query, row)
        db.commit()
        
        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
        
    def addNewTask(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        
        newTask = str(self.taskLineEdit.text())
        data = self.calendarWidget.selectedDate().toPyDate()
        
        query = "INSERT INTO tasks(task, completed, data) VALUES (?,?,?)"
        row = (newTask, "NO", data,)
        
        cursor.execute(query,row)
        db.commit()
        self.updateTaskList(data)
        self.taskLineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())