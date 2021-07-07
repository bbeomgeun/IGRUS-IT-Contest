from PyQt5 import QtCore, QtGui, QtWidgets

class framebutton(QtWidgets.QFrame):
    def __init__(self, parent):
        QtWidgets.QFrame.__init__(self, parent)
        self.signal = False
    clicked = QtCore.pyqtSignal()

    def mouseReleaseEvent(self, null):
        if self.signal == True:
            self.clicked.emit()
            self.signal = False
            
    def mousePressEvent(self, null):
        self.signal = True