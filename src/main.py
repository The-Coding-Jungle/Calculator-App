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
from darkdetect import isDark
from qt_material import apply_stylesheet

darkTheme, lightTheme = 'dark_blue.xml', 'light_blue.xml'
styleNames = ["OS preferred", "light Theme", "dark theme"]

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
    def __init__(self, app) -> None:
        super().__init__()
        self.app = app

        self.historyArray = []
        
        self.initUI()
        self.initMenu()

        self.changeStyle(self.osThemeItem)

        self.show()

    def initUI(self):
        self.mainWid = QWidget()
        self.setCentralWidget(self.mainWid)

        layout = QVBoxLayout()
        self.mainWid.setLayout(layout)

        self.simpleCalculatorWidget = SimpleCalculator(self.historyArray)
        self.advancedCalculatorWidget = AdvancedCalculator(self.historyArray)

        layout.addWidget(self.simpleCalculatorWidget)
        layout.addWidget(self.advancedCalculatorWidget)

        self.advancedCalculatorWidget.hide()

    def switchToNormalModeFunction(self):
        
        self.simpleCalculatorWidget.lineEdit.setText(    
            self.advancedCalculatorWidget.lineEdit.text()
        )
        
        self.advancedCalculatorWidget.hide()
        self.simpleCalculatorWidget.show()
    
    def switchToAdvancedModeFunction(self):
        
        self.advancedCalculatorWidget.lineEdit.setText(
            self.simpleCalculatorWidget.lineEdit.text()
        )
        
        self.simpleCalculatorWidget.hide()
        self.advancedCalculatorWidget.show()

    def changeStyle(self, menuAction):
        global darkTheme, lightTheme
        global styleNames

        if menuAction == self.lightThemeItem:  
            apply_stylesheet(self, lightTheme)
        elif menuAction == self.darkThemeItem:
            apply_stylesheet(self, darkTheme)
        else:
            if isDark():
                apply_stylesheet(self, darkTheme)
            else:
                apply_stylesheet(self, lightTheme)

    def initMenu(self):
        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)

        # Switch mode menu. Start.
        self.switchModeMenu = QMenu("Switch Mode")
        self.menuBar.addMenu(self.switchModeMenu)

        self.normalModeItem = QAction("Normal mode")
        self.switchModeMenu.addAction(self.normalModeItem)
        self.normalModeItem.triggered.connect(self.switchToNormalModeFunction)
        
        self.advancedModeItem = QAction("Advanced Mode")
        self.switchModeMenu.addAction(self.advancedModeItem)
        self.advancedModeItem.triggered.connect(self.switchToAdvancedModeFunction)
        # Switch mode menu. End.

        # Theme menu. Start.
        self.themeMenu = QMenu("Theme")
        self.menuBar.addMenu(self.themeMenu)

        global styleNames

        self.osThemeItem = QAction(styleNames[0])
        self.themeMenu.addAction(self.osThemeItem)
        self.osThemeItem.triggered.connect(lambda: self.changeStyle(self.osThemeItem))

        self.darkThemeItem = QAction(styleNames[1])
        self.themeMenu.addAction(self.darkThemeItem)
        self.darkThemeItem.triggered.connect(lambda: self.changeStyle(self.lightThemeItem))

        self.lightThemeItem = QAction(styleNames[2])
        self.themeMenu.addAction(self.lightThemeItem)
        self.lightThemeItem.triggered.connect(lambda: self.changeStyle(self.darkThemeItem))

class CalculatorApp(QApplication):
    def __init__(self) -> None:
        super().__init__(["Calculator"])
        self.initUI()
        sys.exit(self.exec_())

    def initUI(self):
        self.mainWindow = MainWindow(self)

if __name__ == "__main__":
    app = CalculatorApp()