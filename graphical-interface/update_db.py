# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_db.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_update(object):
    def setupUi(self, update):
        update.setObjectName("update")
        update.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(update)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(40, 10, 121, 28))
        self.pushButton_search.setObjectName("pushButton_search")
        self.scrollArea_students = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_students.setGeometry(QtCore.QRect(300, 10, 281, 271))
        self.scrollArea_students.setWidgetResizable(True)
        self.scrollArea_students.setObjectName("scrollArea_students")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 269))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_students.setWidget(self.scrollAreaWidgetContents)
        self.spinBox_grade = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_grade.setGeometry(QtCore.QRect(140, 240, 60, 22))
        self.spinBox_grade.setMaximum(100)
        self.spinBox_grade.setObjectName("spinBox_grade")
        self.label_surname = QtWidgets.QLabel(self.centralwidget)
        self.label_surname.setGeometry(QtCore.QRect(10, 90, 110, 21))
        self.label_surname.setObjectName("label_surname")
        self.label_age = QtWidgets.QLabel(self.centralwidget)
        self.label_age.setGeometry(QtCore.QRect(10, 140, 110, 21))
        self.label_age.setObjectName("label_age")
        self.lineEdit_surname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_surname.setGeometry(QtCore.QRect(140, 90, 140, 22))
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.label_grade = QtWidgets.QLabel(self.centralwidget)
        self.label_grade.setGeometry(QtCore.QRect(10, 240, 110, 21))
        self.label_grade.setObjectName("label_grade")
        self.label_gender = QtWidgets.QLabel(self.centralwidget)
        self.label_gender.setGeometry(QtCore.QRect(10, 190, 110, 21))
        self.label_gender.setObjectName("label_gender")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(140, 50, 140, 22))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.spinBox_age = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_age.setGeometry(QtCore.QRect(140, 140, 60, 22))
        self.spinBox_age.setObjectName("spinBox_age")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(10, 50, 110, 21))
        self.label_name.setObjectName("label_name")
        self.comboBox_gender = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_gender.setGeometry(QtCore.QRect(140, 190, 100, 22))
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(30, 320, 121, 28))
        self.pushButton_update.setObjectName("pushButton_update")
        self.label_ID = QtWidgets.QLabel(self.centralwidget)
        self.label_ID.setGeometry(QtCore.QRect(10, 280, 110, 21))
        self.label_ID.setObjectName("label_ID")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(140, 280, 71, 22))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        update.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(update)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        update.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(update)
        self.statusbar.setObjectName("statusbar")
        update.setStatusBar(self.statusbar)

        self.retranslateUi(update)
        QtCore.QMetaObject.connectSlotsByName(update)

    def retranslateUi(self, update):
        _translate = QtCore.QCoreApplication.translate
        update.setWindowTitle(_translate("update", "MainWindow"))
        self.pushButton_search.setText(_translate("update", "ყველა მონაცემი"))
        self.label_surname.setText(_translate("update", "გვარი"))
        self.label_age.setText(_translate("update", "ასაკი"))
        self.label_grade.setText(_translate("update", "ნიშანი"))
        self.label_gender.setText(_translate("update", "გენდერი"))
        self.label_name.setText(_translate("update", "სახელი"))
        self.pushButton_update.setText(_translate("update", "განაახლე"))
        self.label_ID.setText(_translate("update", "ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update = QtWidgets.QMainWindow()
    ui = Ui_update()
    ui.setupUi(update)
    update.show()
    sys.exit(app.exec_())
