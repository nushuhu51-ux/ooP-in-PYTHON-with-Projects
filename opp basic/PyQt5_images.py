import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, self.width(), self.height())

        pixmap = QPixmap(
            "C:/Users/Samuel/OneDrive/Desktop/OPP PYTHON/opp basic/photo_2026-07-06_16-11-36.jpg"
        )

        if pixmap.isNull():
            print("Image could not be loaded!")
        else:
            label.setPixmap(pixmap)

        label.setScaledContents(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()