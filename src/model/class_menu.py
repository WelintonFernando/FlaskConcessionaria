from PyQt5.QtWidgets import QApplication, QMainWindow
from pyside2uic.Compiler.qtproxies import QtWidgets

import src.view.mwMenu
from PyQt5 import QtWidgets, uic

from src.view.mwMenu import Ui_MainWindow as ui_mwMenu


class ClassMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = ui_mwMenu()
        self.ui.setupUi(self)




