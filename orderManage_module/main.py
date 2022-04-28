import sys
from PyQt5.QtWidgets import QApplication
from cart import Cart
if __name__ == '__main__':

    app = QApplication(sys.argv)
    testdict = {0: 1, 3: 7,5:2};
    ex = Cart(testdict)
    ex.show()
    sys.exit(app.exec_())