from example_module.ui_example_widget import Ui_Form
from PyQt5.QtWidgets import QWidget

class ExampleWidget(QWidget, Ui_Form):
    def _init__(self, parent=None):
        super(ExampleWidget, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_ex.clicked.connect(self.set_text)


    def set_text(self):
        self.plainTextEdit_ex.setPlainText("Hello World!")

