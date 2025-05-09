import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor


class SortCanvas(QWidget):
    def __init__(self, array):
        super().__init__()
        self.array = array
        self.highlight = {}

    def paintEvent(self, event):
        painter = QPainter(self)
        width = self.width() // len(self.array)
        for i, val in enumerate(self.array):
            color = self.highlight.get(i, QColor("white"))
            painter.setBrush(color)
            painter.drawRect(i * width, self.height() - val, width, val)


class SortApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sort Visualizer")
        self.setGeometry(100, 100, 800, 600)

        self.array = [random.randint(10, 500) for _ in range(100)]
        self.canvas = SortCanvas(self.array)

        self.sort_btn = QPushButton("Avvia Bubble Sort")
        self.sort_btn.clicked.connect(self.start_sort)

        self.reset_btn = QPushButton("Reset Array")
        self.reset_btn.clicked.connect(self.reset_array)

        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 100)
        self.speed_slider.setValue(50)

        self.label = QLabel("Velocità")

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.sort_btn)
        layout.addWidget(self.reset_btn)
        layout.addWidget(self.label)
        layout.addWidget(self.speed_slider)
        self.setLayout(layout)

        self.sorting = False

    def reset_array(self):
        if not self.sorting:
            self.array = [random.randint(10, 500) for _ in range(100)]
            self.canvas.array = self.array
            self.canvas.highlight = {}
            self.canvas.repaint()

    def start_sort(self):
        if self.sorting:
            return
        self.sorting = True
        self.bubble_sort()

    def bubble_sort(self):
        def sort_step():
            nonlocal i, j
            if i < n:
                if j < n - i - 1:
                    self.canvas.highlight = {j: QColor("red"), j + 1: QColor("red")}
                    if self.array[j] > self.array[j + 1]:
                        self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    j += 1
                    self.canvas.repaint()
                else:
                    i += 1
                    j = 0
            else:
                self.canvas.highlight = {}
                self.canvas.repaint()
                timer.stop()
                self.sorting = False

        i, j = 0, 0
        n = len(self.array)
        timer = QTimer()
        timer.timeout.connect(sort_step)
        delay = 101 - self.speed_slider.value()  # 1-100 slider → 100-1 delay
        timer.start(delay)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortApp()
    window.show()
    sys.exit(app.exec_())
