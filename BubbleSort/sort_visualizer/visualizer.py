from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSlider, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QTimer
import random

class SortCanvas(QWidget):
    def __init__(self, parent, array):
        super().__init__(parent)
        self.parent = parent
        self.array = array
        self.highlight = {}
        self.sorting = False
        self.RED = QColor(255, 0, 0)
        self.DEFAULT = QColor(173, 216, 230)  # Light blue

    def paintEvent(self, event):
        painter = QPainter(self)
        width = self.width() / len(self.array or [1])
        height = self.height()
        for i, val in enumerate(self.array):
            color = self.highlight.get(i, self.DEFAULT)
            painter.setBrush(color)
            painter.drawRect(int(i * width), height - val, int(width), val)

    def update_array(self, new_array):
        self.array = new_array
        self.highlight = {}
        self.repaint()


class SortApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎨 Sorting Algorithm Visualizer")
        self.setGeometry(100, 100, 1000, 600)

        self.array = [random.randint(10, 500) for _ in range(100)]
        self.canvas = SortCanvas(self, self.array)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Controls
        controls = QHBoxLayout()
        self.start_btn = QPushButton("▶ Avvia Bubble Sort")
        self.reset_btn = QPushButton("🔄 Reset Array")
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 100)
        self.speed_slider.setValue(50)
        speed_label = QLabel("Velocità:")

        controls.addWidget(self.start_btn)
        controls.addWidget(self.reset_btn)
        controls.addWidget(speed_label)
        controls.addWidget(self.speed_slider)

        # Connect buttons
        self.start_btn.clicked.connect(self.start_bubble_sort)
        self.reset_btn.clicked.connect(self.reset_array)

        layout.addWidget(self.canvas)
        layout.addLayout(controls)
        self.setLayout(layout)

    def reset_array(self):
        if not self.canvas.sorting:
            self.array = [random.randint(10, 500) for _ in range(100)]
            self.canvas.update_array(self.array)

    def start_bubble_sort(self):
        if self.canvas.sorting:
            return
        self.canvas.sorting = True
        from algorithms import bubble_sort
        bubble_sort(self.canvas, self.array, speed=(101 - self.speed_slider.value()) / 1000)