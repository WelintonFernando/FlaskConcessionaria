import PyQt5
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from src.model.class_menu import ClassMenu


class App(QApplication):
    def __init__(self, argv):
        super(App, self).__init__(argv)
        self.main_view = ClassMenu()
        self.main_view.show()


if __name__ == "__main__":
    import sys
    app = App(sys.argv)
    sys.exit(app.exec_())

