from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(571, 433)
        self.pushButton_ex = QtWidgets.QPushButton(Form)
        self.pushButton_ex.setGeometry(QtCore.QRect(210, 250, 81, 61))
        self.pushButton_ex.setObjectName("pushButton_ex")
        self.plainTextEdit_ex = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_ex.setGeometry(QtCore.QRect(180, 90, 151, 101))
        self.plainTextEdit_ex.setObjectName("plainTextEdit_ex")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_ex.setText(_translate("Form", "PushButton"))
