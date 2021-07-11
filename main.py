import sys
from PyQt5.QtWidgets import QApplication

from UI.ui_main_window import MainWindowUI


def main():
    app = QApplication(sys.argv)
    ex = MainWindowUI()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
