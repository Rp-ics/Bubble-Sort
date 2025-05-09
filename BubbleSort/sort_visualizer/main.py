import sys
import os
# Aggiunge la directory principale al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from PyQt5.QtWidgets import QApplication
from visualizer import SortApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortApp()
    window.show()
    sys.exit(app.exec_())