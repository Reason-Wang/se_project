# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\l\Desktop\软工大作业\se_project\StoreManage\ui\updatePage\updatePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(553, 520)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Piclabel = QtWidgets.QLabel(Form)
        self.Piclabel.setMinimumSize(QtCore.QSize(171, 271))
        self.Piclabel.setObjectName("Piclabel")
        self.gridLayout_2.addWidget(self.Piclabel, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ChangePicButton = QtWidgets.QPushButton(Form)
        self.ChangePicButton.setMinimumSize(QtCore.QSize(93, 28))
        self.ChangePicButton.setMaximumSize(QtCore.QSize(93, 28))
        self.ChangePicButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ChangePicButton.setObjectName("ChangePicButton")
        self.horizontalLayout.addWidget(self.ChangePicButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(79, 80))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(Form)
        self.nameEdit.setMinimumSize(QtCore.QSize(158, 24))
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(79, 79))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.priceEdit = QtWidgets.QLineEdit(Form)
        self.priceEdit.setMinimumSize(QtCore.QSize(158, 24))
        self.priceEdit.setObjectName("priceEdit")
        self.gridLayout.addWidget(self.priceEdit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(79, 80))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.numberEdit = QtWidgets.QLineEdit(Form)
        self.numberEdit.setMinimumSize(QtCore.QSize(158, 24))
        self.numberEdit.setObjectName("numberEdit")
        self.gridLayout.addWidget(self.numberEdit, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(79, 79))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.catEdit = QtWidgets.QLineEdit(Form)
        self.catEdit.setMinimumSize(QtCore.QSize(158, 24))
        self.catEdit.setObjectName("catEdit")
        self.gridLayout.addWidget(self.catEdit, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.OKpushButton = QtWidgets.QPushButton(Form)
        self.OKpushButton.setMinimumSize(QtCore.QSize(111, 28))
        self.OKpushButton.setObjectName("OKpushButton")
        self.horizontalLayout_2.addWidget(self.OKpushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.CancelpushButton = QtWidgets.QPushButton(Form)
        self.CancelpushButton.setMinimumSize(QtCore.QSize(111, 28))
        self.CancelpushButton.setObjectName("CancelpushButton")
        self.horizontalLayout_2.addWidget(self.CancelpushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "商品详情"))
        self.Piclabel.setText(_translate("Form", "商品图片"))
        self.ChangePicButton.setText(_translate("Form", "修改图片"))
        self.label_2.setText(_translate("Form", "商品名称"))
        self.label_3.setText(_translate("Form", "商品价格"))
        self.label_4.setText(_translate("Form", "商品数量"))
        self.label_5.setText(_translate("Form", "商品种类"))
        self.OKpushButton.setText(_translate("Form", "确定"))
        self.CancelpushButton.setText(_translate("Form", "取消"))
