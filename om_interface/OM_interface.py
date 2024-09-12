from pathlib import Path
import sys
 
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)
from PyQt6 import QtWidgets
from PyQt6.uic import loadUi

# from GUI.generated.mainwindow_ui import Ui_MainWindow

    

class Window(QMainWindow):
    comboSelectPortA: QtWidgets.QComboBox
    comboSpeedPortA: QtWidgets.QComboBox
    
    def __init__(self):
        super().__init__()
        ui_path: Path = Path(__file__).parent.joinpath('GUI', 'mainwindow.ui')
        loadUi(ui_path, self)
        # self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.action_About.triggered.connect(self.about)

    def about(self):
        QMessageBox.about(
            self,
            "About OM communication",
            "<p>An \"OM communication\" is an app made to control Orientation Module.</p>"
            "<p>It allows you to:<ul>"
            "<li>get/set sensors and module parameters;</li>"
            "<li>get Horizon (HS) and Sun (SS) sensor images and data;</li>"
            "<li>get Gyro, Accel and Mag data (GAM);</li>"
            "</ul></p>"
        )   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())