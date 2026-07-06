import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setGeometry(700, 300, 500, 500)
    def initUI(self):
        centeral_widget = QWidget()
        self.setCentralWidget(centeral_widget)
        
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        
        label1.setStyleSheet("backgroung-color: red,")
        label2.setStyleSheet("backgroung-color: yellow,") 
        label3.setStyleSheet("backgroung-color: green,") 
        label4.setStyleSheet("backgroung-color: blue,") 
        label5.setStyleSheet("backgroung-color: purple,") 
        
        vbox = QVBoxLayout()
        
        vbox.addWidget(label1, 0, 0)
        vbox.addWidget(label2, 0, 1)
        vbox.addWidget(label3, 1, 0)
        vbox.addWidget(label4, 1, 1)
        vbox.addWidget(label5, 1, 2)
        
        centeral_widget.setLayout(vbox)
        
        label = QLabel(self)
        label.setGeometry(0, 0, 500, 500)



def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
        
        if __name__ == "__main__":
            main()