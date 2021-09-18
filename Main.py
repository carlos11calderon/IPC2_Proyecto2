from Gestor import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Interfaz import Ui_Ensamblador
gestor = Gestor()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ensamblador = QtWidgets.QMainWindow()
    ui = Ui_Ensamblador()
    ui.setupUi(Ensamblador)
    Ensamblador.show()
    sys.exit(app.exec_())


    