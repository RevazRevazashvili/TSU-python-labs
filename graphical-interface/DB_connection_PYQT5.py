import os
import sqlite3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QMessageBox
from connect_db import Ui_connect
from insert_db import Ui_insert
from select_db import Ui_select
from update_db import Ui_update
from delete_db import Ui_delete_2

# ბრძანება რომლითან UI გაფართოების ფაილი გარდაიქმნება py გაფართოების ფაილად
# pyuic5 -x insert_db.ui -o insert_db.py


class insert2DB(QtWidgets.QMainWindow):
    def __init__(self, conn, cursor):
        super().__init__()
        self.ui = Ui_insert()
        self.ui.setupUi(self)
        self.cursor = cursor
        self.conn = conn
        self.ui.comboBox_gender.addItems(['მამრობითი', 'მდედრობითი', 'სხვა'])
        self.ui.pushButton_insert.clicked.connect(self.insertDB)
        self.show()

    def insertDB(self):
        name = self.ui.lineEdit_name.text()
        age = self.ui.spinBox_age.value()
        gender = self.ui.comboBox_gender.currentText()
        surname = self.ui.lineEdit_surname.text()
        grade = self.ui.spinBox_grade.value()
        print(name, age, gender, surname, grade)

        try:
            comm = """
                        CREATE TABLE IF NOT EXISTS Student(
                            Id INTEGER PRIMARY KEY,
                            LName TEXT,
                            FName TEXT,
                            Age INTEGER,
                            Gender TEXT,
                            Grade INTEGER
                        )
                    """
            self.cursor.execute(comm)
            insert_comm = """
                        INSERT INTO Student (LName, FName, Age, Gender, Grade) 
                        VALUES (?, ?, ?, ?, ?)
                    """
            self.cursor.execute(insert_comm, (surname, name, age, gender, grade))
            self.conn.commit()
            QtWidgets.QMessageBox.information(self, 'Success', 'მონაცემები დაემატა წარმატებით!')
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, 'Error', f'წარმოიშვა შეცდომა: {str(e)}')
        self.close()


class selectDB(QtWidgets.QMainWindow):
    def __init__(self, conn, cursor):
        super().__init__()
        self.ui = Ui_select()
        self.ui.setupUi(self)
        self.cursor = cursor
        self.conn = conn
        self.ui.comboBox_search_type.addItems(['სახელით', 'გვარით', 'ასაკით', 'სქესით', 'ნიშნით'])
        self.ui.pushButton_search.clicked.connect(self.selectDB)
        self.show()


    def selectDB(self):
        type = self.ui.comboBox_search_type.currentText()

        by = self.ui.lineEdit_search_by.text()

        if type == 'სახელით':
            self.cursor.execute("SELECT * FROM Student WHERE FName = ?", (by,))
            results = self.cursor.fetchall()
            self.displayTextInScrollArea(results)

        if type == 'გვარით':
            self.cursor.execute("SELECT * FROM Student WHERE LName = ?", (by,))
            results = self.cursor.fetchall()
            self.displayTextInScrollArea(results)

        if type == 'ასაკით':
            self.cursor.execute("SELECT * FROM Student WHERE Age = ?", (by,))
            results = self.cursor.fetchall()
            self.displayTextInScrollArea(results)

        if type == 'სქესით':
            self.cursor.execute("SELECT * FROM Student WHERE Gender = ?", (by,))
            results = self.cursor.fetchall()
            self.displayTextInScrollArea(results)

        if type == 'ნიშნით':
            self.cursor.execute("SELECT * FROM Student WHERE Grade = ?", (by,))
            results = self.cursor.fetchall()
            self.displayTextInScrollArea(results)

    def displayTextInScrollArea(self, results):
        scrollArea = self.ui.scrollArea_students
        contentWidget = QtWidgets.QWidget()
        layout = QVBoxLayout(contentWidget)

        for result in results:
            label = QLabel(str(result))
            label.setWordWrap(True)
            layout.addWidget(label)

        contentWidget.setLayout(layout)
        scrollArea.setWidget(contentWidget)


class updateDB(QtWidgets.QMainWindow):
    def __init__(self, conn, cursor):
        super().__init__()
        self.ui = Ui_update()
        self.ui.setupUi(self)
        self.cursor = cursor
        self.conn = conn
        self.ui.comboBox_gender.addItems(['მამრობითი', 'მდედრობითი', 'სხვა'])
        self.ui.pushButton_search.clicked.connect(self.printall)
        self.ui.pushButton_update.clicked.connect(self.updateDB)
        self.show()


    def printall(self):
        self.cursor.execute("SELECT * FROM Student")
        results = self.cursor.fetchall()
        self.displayTextInScrollArea(results)

    def updateDB(self, ):
        name = self.ui.lineEdit_name.text()
        age = self.ui.spinBox_age.value()
        gender = self.ui.comboBox_gender.currentText()
        surname = self.ui.lineEdit_surname.text()
        grade = self.ui.spinBox_grade.value()
        ID = self.ui.lineEdit_ID.text()

        if ID == '':
            QtWidgets.QMessageBox.critical(self, 'Error', 'წარმოიშვა შეცდომა: შეავსეთ ID ველი')
        else:
            try:
                self.cursor.execute("""
                    UPDATE Student SET 
                    FName = ?, 
                    LName = ?, 
                    Age = ?, 
                    Gender = ?, 
                    Grade = ? 
                    WHERE Id = ?
                """, (name, surname, age, gender, grade, ID))
                self.conn.commit()
                QtWidgets.QMessageBox.information(self, 'Success', 'მონაცემები წარმატებით განახლდა')
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, 'Error', f'წარმოიშვა შეცდომა: {str(e)}')

    def displayTextInScrollArea(self, results):
        scrollArea = self.ui.scrollArea_students
        contentWidget = QtWidgets.QWidget()
        layout = QVBoxLayout(contentWidget)

        for result in results:
            label = QLabel(str(result))
            label.setWordWrap(True)
            layout.addWidget(label)

        contentWidget.setLayout(layout)
        scrollArea.setWidget(contentWidget)


class deleteDB(QtWidgets.QMainWindow):
    def __init__(self, conn, cursor):
        super().__init__()
        self.ui = Ui_delete_2()
        self.ui.setupUi(self)
        self.cursor = cursor
        self.conn = conn
        self.ui.pushButton_search.clicked.connect(self.printall)
        self.ui.pushButton_delete.clicked.connect(self.deleteDB)
        self.ui.pushButton_deleteall.clicked.connect(self.deleteallDB)
        self.show()


    def printall(self):
        self.cursor.execute("SELECT * FROM Student")
        results = self.cursor.fetchall()
        self.displayTextInScrollArea(results)

    def displayTextInScrollArea(self, results):
        scrollArea = self.ui.scrollArea_students
        contentWidget = QtWidgets.QWidget()
        layout = QVBoxLayout(contentWidget)

        for result in results:
            label = QLabel(str(result))
            label.setWordWrap(True)
            layout.addWidget(label)

        contentWidget.setLayout(layout)
        scrollArea.setWidget(contentWidget)

    def deleteallDB(self):
        reply = QMessageBox.question(
            self, 'Confirmation',
            'ნამდვილად გსურთ ყველა მონაცემის წაშლა?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.cursor.execute("DELETE FROM Student")
            self.conn.commit()

    def deleteDB(self):
        ID = self.ui.lineEdit_ID.text()

        if ID == '':
            QtWidgets.QMessageBox.critical(self, 'Error', 'წარმოიშვა შეცდომა: შეავსეთ ID ველი')
        else:
            try:
                self.cursor.execute("""DELETE FROM Student WHERE Id = ?""", (ID,))
                self.conn.commit()
                QtWidgets.QMessageBox.information(self, 'Success', 'ველი წარმატებით წაიშალა')
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, 'Error', f'წარმოიშვა შეცდომა: {str(e)}')


class connect2DB(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_connect()
        self.ui.setupUi(self)
        self.ui.pushButton_connect.clicked.connect(self.connect)
        self.ui.pushButton_add.clicked.connect(self.insertButt)
        self.ui.pushButton_select.clicked.connect(self.selectButt)
        self.ui.pushButton_update.clicked.connect(self.updateButt)
        self.ui.pushButton_delete.clicked.connect(self.deleteButt)
        self.ui.pushButton_add.setEnabled(False)
        self.ui.pushButton_update.setEnabled(False)
        self.ui.pushButton_delete.setEnabled(False)
        self.ui.pushButton_select.setEnabled(False)
        self.show()


    def connect(self):
        self.dbName = self.ui.lineEdit_connect.text()
        try:
            self.conn = sqlite3.connect(os.getcwd() + '/' + self.dbName+".db")
            self.cursor = self.conn.cursor()
            self.ui.label_status.setText(f"წარმატებით დაკავშირდა {self.dbName} ბაზასთან")
            self.ui.label_status.setStyleSheet("color: rgb(0, 150, 0);")
            self.ui.label_status.adjustSize()
            self.ui.pushButton_add.setEnabled(True)
            self.ui.pushButton_select.setEnabled(True)
            self.ui.pushButton_update.setEnabled(True)
            self.ui.pushButton_delete.setEnabled(True)
        except:
            self.ui.label_status.setText(f"{self.dbName} ბაზასთან ვერ დაკავშირდა")
            self.ui.label_status.setStyleSheet("color: rgb(150, 0, 0);")
            self.ui.label_status.adjustSize()

    def insertButt(self):
        self.insertWindow = insert2DB(self.conn, self.cursor)
        self.insertWindow.show()

    def selectButt(self):
        self.insertWindow = selectDB(self.conn, self.cursor)
        self.insertWindow.show()

    def updateButt(self):
        self.insertWindow = updateDB(self.conn, self.cursor)
        self.insertWindow.show()

    def deleteButt(self):
        self.insertWindow = deleteDB(self.conn, self.cursor)
        self.insertWindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = connect2DB()
    sys.exit(app.exec_())
