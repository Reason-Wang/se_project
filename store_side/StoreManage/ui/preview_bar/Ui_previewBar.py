# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\l\Desktop\软工大作业\se_project\StoreManage\ui\preview_bar\previewBar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(718, 727)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(81, 16))
        self.label.setMaximumSize(QtCore.QSize(81, 16))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutShaiixuan = QtWidgets.QVBoxLayout()
        self.verticalLayoutShaiixuan.setObjectName("verticalLayoutShaiixuan")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutShaiixuan.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(30, 13))
        self.label_2.setMaximumSize(QtCore.QSize(30, 13))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutShaiixuan.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutShaiixuan.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayoutShaiixuan)
        self.verticalLayoutZhonglei = QtWidgets.QVBoxLayout()
        self.verticalLayoutZhonglei.setObjectName("verticalLayoutZhonglei")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutZhonglei.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(45, 13))
        self.label_3.setMaximumSize(QtCore.QSize(45, 13))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutZhonglei.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutZhonglei.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayoutZhonglei)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(256, 29))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(256, 29))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.pushButtonSerch = QtWidgets.QPushButton(Form)
        self.pushButtonSerch.setMinimumSize(QtCore.QSize(93, 28))
        self.pushButtonSerch.setMaximumSize(QtCore.QSize(93, 28))
        self.pushButtonSerch.setObjectName("pushButtonSerch")
        self.horizontalLayout.addWidget(self.pushButtonSerch)
        spacerItem4 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 559))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setStretch(2, 10000)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "商品预览"))
        self.label_2.setText(_translate("Form", "筛选"))
        self.label_3.setText(_translate("Form", "种类："))
        self.pushButtonSerch.setText(_translate("Form", "查询"))