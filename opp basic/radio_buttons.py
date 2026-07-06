import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QRadioButton,
    QButtonGroup,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(700, 300, 500, 500)

        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)

        self.payment_group = QButtonGroup(self)
        self.purchase_group = QButtonGroup(self)

        self.initUI()

    def initUI(self):

        self.radio1.setGeometry(20, 20, 300, 50)
        self.radio2.setGeometry(20, 70, 300, 50)
        self.radio3.setGeometry(20, 120, 300, 50)
        self.radio4.setGeometry(20, 190, 300, 50)
        self.radio5.setGeometry(20, 240, 300, 50)

        self.setStyleSheet("""
            QRadioButton{
                font-size: 24px;
                font-family: Arial;
                padding: 10px;
            }
        """)

        # Payment methods
        self.payment_group.addButton(self.radio1)
        self.payment_group.addButton(self.radio2)
        self.payment_group.addButton(self.radio3)

        # Purchase methods
        self.purchase_group.addButton(self.radio4)
        self.purchase_group.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()

        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()