#imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout,QVBoxLayout,QGridLayout



# App settings
app = QApplication([])
main_windown = QWidget()
main_windown.setWindowTitle("Calculator APP")
main_windown.resize(250,300)



# Widgets/ All objects

text_box = QLineEdit()
grid = QGridLayout()

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","+",
    "0",".","=","-"
           ]


clear = QPushButton("Clear")
delete = QPushButton("<")


def button_clicked():
    button = app.sender()
    text = button.text()

    if text == "=":
        try:
            textBox = text_box.text()
            res = eval(textBox)
            text_box.setText(str(res))
        except Exception as e:
            text_box.setText("Error : " + str(e))
    elif text == "Clear":
        text_box.clear()

    elif text == "<":
         text_box.setText(text_box.text()[:-1])

    else:

        text_box_value = text_box.text()
        text_box.setText(text_box_value + text)





col = 0
row = 0

for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_clicked)
    grid.addWidget(button,row,col)
    col += 1

    if col > 3:
        col = 0
        row += 1


clear.clicked.connect(button_clicked)
delete.clicked.connect(button_clicked)



# Layouts
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout.addLayout(button_row)
# Events



main_windown.setLayout(master_layout)

# Show/Run

main_windown.show()
app.exec()