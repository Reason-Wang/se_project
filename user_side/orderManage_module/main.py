import sys
from PyQt5.QtWidgets import QApplication

from cart import Cart
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Cart()
    ex.changeAccount("小黑")
    #ex=OrderItem(20)
    ex.show()
    #print(1111)
    sys.exit(app.exec_())