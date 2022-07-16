from PyQt5 import QtWidgets
from design import Ui_MainWindow
import sys
import requests
import subprocess


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def load_changelog(self):
        self.ui.Changelog.setText("hi")

    def launch_game(self):
        # TODO: make working
        pass


app = QtWidgets.QApplication([])
application = Window()
application.load_changelog()
application.show()

sys.exit(app.exec())
