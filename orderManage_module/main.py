import sys
from PyQt5.QtWidgets import QApplication
from cart import Cart
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Cart(4)
    ex.show()
    sys.exit(app.exec_())