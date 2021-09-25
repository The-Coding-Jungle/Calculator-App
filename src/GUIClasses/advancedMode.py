from PyQt5.QtWidgets import (
    QWidget
)
from typing import List

class AdvancedCalculator(QWidget):
    def __init__(self, historyArray: List[List[str]], size: List[int]):
        super().__init__()
        self.initUI()
        self.historyArray = historyArray
        self.size = size 

    def initUI(self) -> None:
        pass 