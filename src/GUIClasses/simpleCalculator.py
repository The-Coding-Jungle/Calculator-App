from typing import List
from PyQt5.QtWidgets import (
    QWidget, 
    QLineEdit, 
    QPushButton, 
    QVBoxLayout, 
    QGridLayout,
)

from PyQt5.QtCore import (
    QSize
)

BUTTONS = [
    ['7', '8', '9', '/', 'C'],
    ['4', '5', '6', 'x', '^2'],
    ['1', '2', '3', '-', 'Go Back'],
    ['0', '.', '%', '+', '=']
]

IS_SPECIAL_BUTTON = [
    [False, False, False, False, True],
    [False, False, False, False, True],
    [False, False, False, False, True],
    [False, False, False, False, True]
]

class SimpleCalculator(QWidget):
    def __init__(self, historyArray:List[List[str]], size: List[int]):
        super().__init__()
        self.initUI()
        self.historyArray = historyArray
        self.size = size

    def goBackInHistory(self):
        if len(self.historyArray) == 0:
            self.lineEdit.setText('')
        else:
            toSet = self.historyArray.pop()
            self.lineEdit.setText(toSet)

    def solve(self):
        q = self.lineEdit.text()
        a = str(eval(q))
        self.historyArray.append(q)
        self.lineEdit.setText(a)

    def initUI(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)
    
        self.lineEdit = QLineEdit()
        
        layout.addWidget(self.lineEdit)

        self.buttonsWidget = QWidget()
        
        buttonsLayout = QGridLayout()
        self.buttonsWidget.setLayout(buttonsLayout)

        layout.addWidget(self.buttonsWidget)

        self.buttons = []

        for i in range(4):
            self.buttons.append([])
            for j in range(5):
                curButton = QPushButton(BUTTONS[i][j])
                self.buttons[i].append(curButton)
                buttonsLayout.addWidget(self.buttons[i][j], i, j)
                # Most of the button click should only add the text to the lineEdit.
                if not IS_SPECIAL_BUTTON[i][j]:
                    self.buttons[i][j].clicked.connect(
                        lambda _, i = i, j = j: 
                        self.lineEdit.setText(
                            self.lineEdit.text() + 
                            self.buttons[i][j].text()
                        )
                    )

        # We add functons here for the special buttons.
        # Giving function to 'C' button.
        self.buttons[0][4].clicked.connect(lambda : self.lineEdit.setText(''))

        # Giving function to '^2' function.
        self.buttons[1][4].clicked.connect(lambda : self.lineEdit.setText(self.lineEdit.text() + '**2'))

        # Giving function to 'Go back button'.
        self.buttons[2][4].clicked.connect(lambda : self.goBackInHistory())

        # Giving function to '=' button
        self.buttons[3][4].clicked.connect(lambda : self.solve())
