# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\11487\Desktop\code\se_project\orderManage_module\ui_file\input.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 301)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.nameEdit.setFrame(True)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_4.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.phoneEdit = QtWidgets.QLineEdit(Dialog)
        self.phoneEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.phoneEdit.setObjectName("phoneEdit")
        self.horizontalLayout_3.addWidget(self.phoneEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.addrEdit = QtWidgets.QLineEdit(Dialog)
        self.addrEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.addrEdit.setObjectName("addrEdit")
        self.horizontalLayout_2.addWidget(self.addrEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelBtn = QtWidgets.QPushButton(Dialog)
        self.cancelBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.confirmBtn = QtWidgets.QPushButton(Dialog)
        self.confirmBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.confirmBtn.setObjectName("confirmBtn")
        self.horizontalLayout.addWidget(self.confirmBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "??????"))
        self.label_2.setText(_translate("Dialog", "??????"))
        self.label_3.setText(_translate("Dialog", "??????"))
        self.cancelBtn.setText(_translate("Dialog", "??????"))
        self.confirmBtn.setText(_translate("Dialog", "??????"))
