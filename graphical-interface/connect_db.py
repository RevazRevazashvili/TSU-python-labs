# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_db.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_connect(object):
    def setupUi(self, connect):
        connect.setObjectName("connect")
        connect.resize(512, 402)
        self.centralwidget = QtWidgets.QWidget(connect)
        self.centralwidget.setObjectName("centralwidget")
        self.labe_connect_db = QtWidgets.QLabel(self.centralwidget)
        self.labe_connect_db.setGeometry(QtCore.QRect(180, 40, 130, 31))
        self.labe_connect_db.setObjectName("labe_connect_db")
        self.lineEdit_connect = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_connect.setGeometry(QtCore.QRect(150, 80, 180, 22))
        self.lineEdit_connect.setObjectName("lineEdit_connect")
        self.pushButton_connect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connect.setGeometry(QtCore.QRect(190, 120, 90, 28))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(130, 100, 220, 16))
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(260, 260, 188, 28))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(260, 190, 188, 28))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(50, 260, 188, 28))
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_select = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_select.setGeometry(QtCore.QRect(50, 190, 188, 28))
        self.pushButton_select.setObjectName("pushButton_select")
        connect.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(connect)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 26))
        self.menubar.setObjectName("menubar")
        connect.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(connect)
        self.statusbar.setObjectName("statusbar")
        connect.setStatusBar(self.statusbar)

        self.retranslateUi(connect)
        QtCore.QMetaObject.connectSlotsByName(connect)

    def retranslateUi(self, connect):
        _translate = QtCore.QCoreApplication.translate
        connect.setWindowTitle(_translate("connect", "MainWindow"))
        self.labe_connect_db.setText(_translate("connect", "დაუკავშირდით ბაზას"))
        self.lineEdit_connect.setPlaceholderText(_translate("connect", "ბაზის სახელი"))
        self.pushButton_connect.setText(_translate("connect", "დაკავშირება"))
        self.pushButton_add.setText(_translate("connect", "ელემენტის ჩამატება ბაზაში"))
        self.pushButton_delete.setText(_translate("connect", "ელემენტის წაშლა ბაზიდან"))
        self.pushButton_update.setText(_translate("connect", "ელემენტის განახლება ბაზაში"))
        self.pushButton_select.setText(_translate("connect", "ელემენტის მიღება ბაზიდან"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    connect = QtWidgets.QMainWindow()
    ui = Ui_connect()
    ui.setupUi(connect)
    connect.show()
    sys.exit(app.exec_())
