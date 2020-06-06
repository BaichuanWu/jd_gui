# -*- coding: utf-8 -*-

from gui.main import JDMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = JDMainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
