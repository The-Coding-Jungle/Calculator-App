from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton
)
from typing import List

BUTTONS = [
    ['7', '8', '9', '/', '+', 'C'],
    ['4', '5', '6', '(', ')', 'Go Back'],
    ['1', '2', '3', '-', 'x^2', '|x|'],
    ['0', '.', '%', 'x^y', 'x^(1/2)', '=']
]

IS_SPECIAL_BUTTON = [
    [False, False, False, False, False, True],
    [False, False, False, False, False, True],
    [False, False, False, False, True, True],
    [False, False, True, True, True, True]
]

class AdvancedCalculator(QWidget):
    def __init__(self, historyArray: List[List[str]]) -> None:
        super().__init__()
        
        self.historyArray = historyArray

        self.initUI()

    def goBackInHistory(self) -> None:
        if len(self.historyArray) == 0:
            self.lineEdit.setText('')
        else:
            toSet = self.historyArray.pop()
            self.lineEdit.setText(toSet)

    def solve(self) -> None:
        q = self.lineEdit.text()
        try:
            a = str(eval(q))
        except Exception:
            a = "Wrong expression"
        self.historyArray.append(q)
        self.lineEdit.setText(a)

    def handleMod(self) -> None:
        a = eval(self.lineEdit.text())
        if a < 0:
            a *= -1
        self.lineEdit.setText(a)

    def handlePercentage(self) -> None:
        exp = self.lineEdit.text()
        lenExp = len(exp)
        self.lineEdit.setText(exp[:lenExp - 1] + '/100')

    def initUI(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.lineEdit = QLineEdit()
        layout.addWidget(self.lineEdit)

        self.buttonsWidget = QWidget()
        layout.addWidget(self.buttonsWidget)

        buttonsLayout = QGridLayout()
        self.buttonsWidget.setLayout(buttonsLayout)

        self.buttons = []

        for i in range(4):
            self.buttons.append([])
            for j in range(6):
                button = QPushButton(BUTTONS[i][j])
                self.buttons[i].append(button)
                buttonsLayout.addWidget(self.buttons[i][j], i, j)
                if not IS_SPECIAL_BUTTON[i][j]:
                    self.buttons[i][j].clicked.connect(lambda _, i = i, j = j : self.lineEdit.setText(self.lineEdit.text() + self.buttons[i][j].text()))
            
        # Giving function to 'C' button at 0, 5
        self.buttons[0][5].clicked.connect(lambda: self.lineEdit.setText(''))

        # Giving function to 'Go Back' at 1, 5.
        self.buttons[1][5].clicked.connect(self.goBackInHistory)

        # Giving function to square at 2, 4.
        self.buttons[2][4].clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "**2"))

        # Giving function to mod at 2, 5.
        self.buttons[2][5].clicked.connect(self.handleMod)

        # Giving function to % at 3, 2.
        self.buttons[3][2].clicked.connect(self.handlePercentage)

        # Giving function to x^y at 3, 3.
        self.buttons[3][3].clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "**"))

        # Giving function to x^(1/2) at 3, 4.
        self.buttons[3][4].clicked.connect(lambda: self.lineEdit.setText(self.lineEdit.text() + "**(1/2)"))

        # Giving function to = at 3, 5.
        self.buttons[3][5].clicked.connect(self.solve)