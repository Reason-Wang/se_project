# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\11487\Desktop\code\se_project\orderManage_module\ui_file\pay.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.payMethodBox = QtWidgets.QComboBox(Dialog)
        self.payMethodBox.setGeometry(QtCore.QRect(150, 120, 111, 31))
        self.payMethodBox.setObjectName("payMethodBox")
        self.payMethodBox.addItem("")
        self.payMethodBox.addItem("")
        self.payMethodBox.addItem("")
        self.money_label = QtWidgets.QLabel(Dialog)
        self.money_label.setGeometry(QtCore.QRect(70, 20, 221, 61))
        self.money_label.setObjectName("money_label")
        self.cancelBtn = QtWidgets.QPushButton(Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(40, 200, 131, 41))
        self.cancelBtn.setObjectName("cancelBtn")
        self.confirmBtn = QtWidgets.QPushButton(Dialog)
        self.confirmBtn.setGeometry(QtCore.QRect(210, 200, 131, 41))
        self.confirmBtn.setObjectName("confirmBtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 130, 72, 15))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.payMethodBox.setItemText(0, _translate("Dialog", "一卡通"))
        self.payMethodBox.setItemText(1, _translate("Dialog", "支付宝"))
        self.payMethodBox.setItemText(2, _translate("Dialog", "微信"))
        self.money_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt;\">TextLabel</span></p></body></html>"))
        self.cancelBtn.setText(_translate("Dialog", "取消支付"))
        self.confirmBtn.setText(_translate("Dialog", "确认支付"))
        self.label.setText(_translate("Dialog", "支付方式："))
