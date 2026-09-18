#imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout,QVBoxLayout,QGridLayout
from PyQt5.QtGui import QFont

# Class 

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator APP")
        self.setGeometry(600,150,450,400)


        # Widgets / All objects

        self.text_box = QLineEdit()
        self.text_box.setStyleSheet("""
    QLineEdit {
        font-family: Arial;
        font-size: 16px;
        color: #333333;
        background-color: #FFFFFF;
        border: 2px solid #3498DB;
        border-radius: 8px;
        padding: 8px;
    }
""")
        self.grid = QGridLayout()
        self.buttons = [
                "7","8","9","/",
                "4","5","6","*",
                "1","2","3","+",
                "0",".","=","-"
           ]
        self.clear = QPushButton("C")
        self.delete = QPushButton("<")
        self.clear.setStyleSheet("""
                                                            QPushButton {
                                                                font-family: Arial;
                                                                font-size: 22px;
                                                                font-weight: bold;
                                                                color: red;
                                                                background-color: #383838;
                                                                border-radius: 18px;
                                                                padding: 10px;
                                                                margin: 3px;
                                                            }
                                        
                                                            QPushButton:hover {
                                                                background-color: #4c4c4c;
                                                            }
                                        
                                                            QPushButton:pressed {
                                                                background-color: #242424;
                                                                border: 2px solid red;
                                                            }
                                                        """)
        self.delete.setStyleSheet("""
                                                            QPushButton {
                                                                font-family: Arial;
                                                                font-size: 22px;
                                                                font-weight: bold;
                                                                color: red;
                                                                background-color: #383838;
                                                                border-radius: 18px;
                                                                padding: 10px;
                                                                margin: 3px;
                                                            }
                                        
                                                            QPushButton:hover {
                                                                background-color: #4c4c4c;
                                                            }
                                        
                                                            QPushButton:pressed {
                                                                background-color: #242424;
                                                                border: 2px solid red;
                                                            }
                                                        """)

        self.col = 0
        self.row = 0

        for text in self.buttons:
            if text in "/*+,-":
                button = QPushButton(text)
                button.setStyleSheet("""
                    QPushButton {
                        font-family: Arial;
                        font-size: 22px;
                        font-weight: bold;
                        color: white;
                        background-color: #ff8000;
                        border-radius: 18px;
                        padding: 12px;
                        margin: 3px;
                    }

                    QPushButton:hover {
                        background-color: #ffa057;
                    }

                    QPushButton:pressed {
                        background-color: #ff6400;
                    }
                """)    

                
                button.clicked.connect(self.button_clicked)
                self.grid.addWidget(button,self.row,self.col)

            elif text  == "=":
                button = QPushButton(text)
                button.setStyleSheet("""
                                    QPushButton {
                                        font-family: Arial;
                                        font-size: 22px;
                                        font-weight: bold;
                                        color: white;
                                        background-color: #00aaaa;
                                        border-radius: 18px;
                                        padding: 12px;
                                        margin: 3px;
                                    }
                
                                    QPushButton:hover {
                                        background-color: #32bbbb;
                                    }
                
                                    QPushButton:pressed {
                                        background-color: #004444;
                                    }
                                """)    
                
                                
                button.clicked.connect(self.button_clicked)
                self.grid.addWidget(button,self.row,self.col)

            else:

                button = QPushButton(text)
                button.setStyleSheet("""
                                                    QPushButton {
                                                        font-family: Arial;
                                                        font-size: 22px;
                                                        font-weight: bold;
                                                        color: white;
                                                        background-color: #383838;
                                                        border-radius: 18px;
                                                        padding: 12px;
                                                        margin: 3px;
                                                    }
                                
                                                    QPushButton:hover {
                                                        background-color: #4c4c4c;
                                                    }
                                
                                                    QPushButton:pressed {
                                                        background-color: #242424;
                                                    }
                                                """)
                button.clicked.connect(self.button_clicked)
                self.grid.addWidget(button,self.row,self.col)
            self.col += 1

            if self.col > 3:
                self.col = 0
                self.row += 1


        self.clear.clicked.connect(self.button_clicked)
        self.delete.clicked.connect(self.button_clicked)



        # Layouts
        self.master_layout = QVBoxLayout()
        self.master_layout.addWidget(self.text_box)

        self.button_row = QHBoxLayout()
        self.button_row.addWidget(self.clear)
        self.button_row.addWidget(self.delete)
        
        self.master_layout.addLayout(self.button_row)


        self.master_layout.addLayout(self.grid)

        
        # Events



        self.setLayout(self.master_layout)


    def button_clicked(self):
        self.button = self.sender()
        self.text = self.button.text()

        if self.text == "=":
            try:
                self.testBox = self.text_box.text()
                self.res = eval(self.testBox)
                self.text_box.setText(str(self.res))
            except Exception as e:
                self.text_box.setText("Error : " + str(e))
        elif self.text == "C":
            self.text_box.clear()
        elif self.text == "<":
            self.text_box.setText(self.text_box.text()[:-1])

        else:
            self.text_box_value = self.text_box.text()
            self.text_box.setText(self.text_box_value + self.text)




if __name__ in "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget { background-color: #000000}")
    main_window.show()
    app.exec()
