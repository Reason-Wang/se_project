import sys
from PyQt5.QtWidgets import QApplication

from cart import Cart
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Cart("20191234")
    #ex=OrderItem(20)
    ex.show()
    #print(1111)
    sys.exit(app.exec_())