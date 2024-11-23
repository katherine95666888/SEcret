from PyQt5.QtWidgets import (
    QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QComboBox, QTextEdit
)
from algorithms.opt import opt_replacement
from algorithms.fifo import fifo_replacement
from algorithms.lru import lru_replacement

class PageReplacementUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("页面置换算法实验")
        self.setGeometry(100, 100, 600, 400)

        self.pages_input = QLineEdit(self)
        self.pages_input.setPlaceholderText("输入页面序列（用逗号分隔，如 1,2,3,4,1,2）")

        self.frame_input = QLineEdit(self)
        self.frame_input.setPlaceholderText("输入页框数（如 3）")

        self.algorithm_selector = QComboBox(self)
        self.algorithm_selector.addItems(["OPT", "FIFO", "LRU"])

        self.result_display = QTextEdit(self)
        self.result_display.setReadOnly(True)

        self.run_button = QPushButton("运行算法", self)
        self.run_button.clicked.connect(self.run_algorithm)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("页面序列输入："))
        layout.addWidget(self.pages_input)
        layout.addWidget(QLabel("页框数输入："))
        layout.addWidget(self.frame_input)
        layout.addWidget(QLabel("选择算法："))
        layout.addWidget(self.algorithm_selector)
        layout.addWidget(self.run_button)
        layout.addWidget(QLabel("结果输出："))
        layout.addWidget(self.result_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_algorithm(self):
        try:
            pages = list(map(int, self.pages_input.text().split(",")))
            frame_count = int(self.frame_input.text())
            algorithm = self.algorithm_selector.currentText()

            if algorithm == "OPT":
                faults, results = opt_replacement(pages, frame_count)
            elif algorithm == "FIFO":
                faults, results = fifo_replacement(pages, frame_count)
            elif algorithm == "LRU":
                faults, results = lru_replacement(pages, frame_count)
            else:
                self.result_display.setText("未知算法！")
                return

            output = f"缺页次数: {faults}\n缺页率: {faults / len(pages):.2%}\n\n"
            output += "页面置换过程：\n"
            for i, step in enumerate(results):
                output += f"步骤 {i + 1}: {step}\n"
            self.result_display.setText(output)

        except ValueError:
            self.result_display.setText("输入格式错误！请确保页面序列和页框数为数字。")

