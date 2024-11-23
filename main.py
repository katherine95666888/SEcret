import sys
from PyQt5.QtWidgets import QApplication
from ui.ui_main import PageReplacementUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PageReplacementUI()
    window.show()
    sys.exit(app.exec_())

