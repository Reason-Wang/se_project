# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\11487\Desktop\code\se_project\orderManage_module\ui_file\detail.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 420)
        self.mer_table = QtWidgets.QTableWidget(Form)
        self.mer_table.setGeometry(QtCore.QRect(0, 0, 500, 250))
        self.mer_table.setObjectName("mer_table")
        self.mer_table.setColumnCount(4)
        self.mer_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mer_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mer_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mer_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.mer_table.setHorizontalHeaderItem(3, item)
        self.total_label = QtWidgets.QLabel(Form)
        self.total_label.setGeometry(QtCore.QRect(299, 250, 201, 50))
        self.total_label.setFrameShape(QtWidgets.QFrame.Box)
        self.total_label.setObjectName("total_label")
        self.id_label = QtWidgets.QLabel(Form)
        self.id_label.setGeometry(QtCore.QRect(0, 250, 301, 50))
        self.id_label.setFrameShape(QtWidgets.QFrame.Box)
        self.id_label.setObjectName("id_label")
        self.con_label = QtWidgets.QLabel(Form)
        self.con_label.setGeometry(QtCore.QRect(0, 300, 500, 50))
        self.con_label.setFrameShape(QtWidgets.QFrame.Box)
        self.con_label.setObjectName("con_label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 360, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.status_label = QtWidgets.QLabel(Form)
        self.status_label.setGeometry(QtCore.QRect(0, 350, 301, 50))
        self.status_label.setFrameShape(QtWidgets.QFrame.Box)
        self.status_label.setObjectName("status_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.mer_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "????????????"))
        item = self.mer_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "?????????"))
        item = self.mer_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "??????"))
        item = self.mer_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "????????????"))
        self.total_label.setText(_translate("Form", "????????????"))
        self.id_label.setText(_translate("Form", "???????????????"))
        self.con_label.setText(_translate("Form", "??????????????????"))
        self.pushButton.setText(_translate("Form", "??????"))
        self.status_label.setText(_translate("Form", "???????????????"))
