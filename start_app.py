#start_app.py
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
rc = app.exec_()
sys.exit(rc)
