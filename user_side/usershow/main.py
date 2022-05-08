import sys
from PyQt5.QtWidgets import QApplication
from usershow.setUsershow import myusershow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myusershow()
    #ex=CheckOrder(1,2)
    ex.show()
    sys.exit(app.exec_())