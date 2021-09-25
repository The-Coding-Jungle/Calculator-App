from tkinter.constants import S
from typing import Tuple
from src.GUIClasses import *  
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QMenuBar,
    QMenu,
    QAction
)
from src.AdditionalFunctions.GetScreenSize import getScreenSize
import sys

# Deciding app size has per screen size.
size = [0, 0]
screenSize = getScreenSize()

if screenSize[0] > 1000:
    size[0] = screenSize[0] // 2
else: 
    size[0] = screenSize[0]

if screenSize[1] > 500:
    size[1] = screenSize[1] // 2
else:
    size[1] = screenSize[1]

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.historyArray = []

        self.initUI()
        self.initMenu()

        self.show()

    def initUI(self):
        self.mainWid = QWidget()
        self.setCentralWidget(self.mainWid)

        layout = QVBoxLayout()
        self.mainWid.setLayout(layout)

        self.simpleCalculatorWidget = SimpleCalculator(self.historyArray, size)
        self.advancedCalculatorWidget = AdvancedCalculator(self.historyArray, size)

        layout.addWidget(self.simpleCalculatorWidget)
        layout.addWidget(self.advancedCalculatorWidget)

        self.advancedCalculatorWidget.hide()

    def switchToNormalModeFunction(self):
        '''
        self.simpleCalculatorWidget.lineEdit.setText(    
            self.advancedCalculatorWidget.lineEdit.text()
        )
        '''
        self.advancedCalculatorWidget.hide()
        self.simpleCalculatorWidget.show()
    
    def switchToAdvancedModeFunction(self):
        '''
        self.advancedCalculatorWidget.lineEdit.setText(
            self.simpleCalculatorWidget.lineEdit.text()
        )
        '''
        self.simpleCalculatorWidget.hide()
        self.advancedCalculatorWidget.show()

    def initMenu(self):
        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)

        self.switchModeMenu = QMenu("Switch Mode")
        self.menuBar.addMenu(self.switchModeMenu)

        self.normalModeItem = QAction("Normal mode")
        self.switchModeMenu.addAction(self.normalModeItem)
        self.normalModeItem.triggered.connect(self.switchToNormalModeFunction)
        
        self.advancedModeItem = QAction("Advanced Mode")
        self.switchModeMenu.addAction(self.advancedModeItem)
        self.advancedModeItem.triggered.connect(self.switchToAdvancedModeFunction)

class CalculatorApp(QApplication):
    def __init__(self) -> None:
        super().__init__(["Calculator"])
        self.initUI()
        sys.exit(self.exec_())

    def initUI(self):
        self.mainWindow = MainWindow()

if __name__ == "__main__":
    app = CalculatorApp()