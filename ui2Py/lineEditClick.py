from PyQt5 import QtCore, QtGui, QtWidgets
class lineEditbutton(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.signal = False
    clicked = QtCore.pyqtSignal()
    released = QtCore.pyqtSignal()

    def keyReleaseEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter):
            self.released.emit()

    def mouseReleaseEvent(self, null):
        if self.signal == True:
            self.clicked.emit()
            self.signal = False
            
    def mousePressEvent(self, null):
        self.signal = True