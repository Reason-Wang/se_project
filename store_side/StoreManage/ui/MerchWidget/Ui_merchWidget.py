# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\l\Desktop\软工大作业\se_project\StoreManage\ui\MerchWidget\merchWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(547, 177)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.picture = QtWidgets.QLabel(Form)
        self.picture.setMinimumSize(QtCore.QSize(120, 153))
        self.picture.setFrameShape(QtWidgets.QFrame.Box)
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.gridLayout.addWidget(self.picture, 0, 0, 4, 1)
        self.numberlabel = QtWidgets.QLabel(Form)
        self.numberlabel.setMinimumSize(QtCore.QSize(120, 33))
        self.numberlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.numberlabel.setObjectName("numberlabel")
        self.gridLayout.addWidget(self.numberlabel, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(120, 33))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.pricelabel = QtWidgets.QLabel(Form)
        self.pricelabel.setMinimumSize(QtCore.QSize(120, 33))
        self.pricelabel.setFrameShape(QtWidgets.QFrame.Box)
        self.pricelabel.setObjectName("pricelabel")
        self.gridLayout.addWidget(self.pricelabel, 2, 1, 1, 1)
        self.namelable = QtWidgets.QLabel(Form)
        self.namelable.setMinimumSize(QtCore.QSize(120, 33))
        self.namelable.setFrameShape(QtWidgets.QFrame.Box)
        self.namelable.setObjectName("namelable")
        self.gridLayout.addWidget(self.namelable, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonUpdate = QtWidgets.QPushButton(Form)
        self.pushButtonUpdate.setMaximumSize(QtCore.QSize(137, 28))
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.verticalLayout.addWidget(self.pushButtonUpdate)
        self.pushButtonDelete = QtWidgets.QPushButton(Form)
        self.pushButtonDelete.setMaximumSize(QtCore.QSize(137, 28))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.verticalLayout.addWidget(self.pushButtonDelete)
        self.pushButtonUpdatePIC = QtWidgets.QPushButton(Form)
        self.pushButtonUpdatePIC.setObjectName("pushButtonUpdatePIC")
        self.verticalLayout.addWidget(self.pushButtonUpdatePIC)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.numberlabel.setText(_translate("Form", "商品库存"))
        self.label_5.setText(_translate("Form", "商品类别"))
        self.pricelabel.setText(_translate("Form", "商品价格"))
        self.namelable.setText(_translate("Form", "商品名称"))
        self.pushButtonUpdate.setText(_translate("Form", "修改商品信息"))
        self.pushButtonDelete.setText(_translate("Form", "下架商品"))
        self.pushButtonUpdatePIC.setText(_translate("Form", "修改图片"))
        self.pushButton.setText(_translate("Form", "查看/修改详情"))
