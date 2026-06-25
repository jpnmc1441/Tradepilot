import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow
from core.application import Application


def main():

    application = Application()

    application.start()

    qt = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(qt.exec())


if __name__ == "__main__":
    main()
