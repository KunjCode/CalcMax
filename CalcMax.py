import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon

class CalcMax(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CalcMax")
        self.setWindowIcon(QIcon("1.ico"))

        self.setStyleSheet("background-color: darkgray;")

        self.setStyleSheet("color: blue")
        
        self.setGeometry(500, 500, 400, 400)

        self.create_layout()

    def create_layout(self):

        vbox = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        vbox.addWidget(self.display)


        grid = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('AC',4, 1), ('DEL', 4, 2)
        ]


        for btn_txt, row, col in buttons:
            button = QPushButton(btn_txt)

            if btn_txt in ['+', '-', '*', '/']:  # Operator buttons
                button.setStyleSheet("background-color: orange; color: white; font-size: 16px;")
            elif btn_txt == '=':  # Equal button
                button.setStyleSheet("background-color: green; color: white; font-size: 16px;")
            elif btn_txt == 'AC':
                button.setStyleSheet("background-color: red; color: black; font-size: 16px; bold")
            elif btn_txt == 'DEL':
                button.setStyleSheet("background-color: red; color: black; font-size: 16px; bold")
            else:  # Numeric and decimal buttons
                button.setStyleSheet("background-color: lightblue; color: black; font-size: 16px;")

            button.clicked.connect(self.on_button_clicked)
            grid.addWidget(button, row, col)
            


        vbox.addLayout(grid)

        self.setLayout(vbox)

    def on_button_clicked(self):

        button = self.sender()
        btn_text = button.text()

        if btn_text == '=':
            try:
                expression = self.display.text()
                result = str(eval(expression))
                self.display.setText(result)
            except:
                self.display.setText("Error")

        elif btn_text == "AC":
            self.display.clear()

        elif btn_text == "DEL":
            self.display.backspace()

        else:
            self.display.setText(self.display.text() + btn_text)



def main():
    app = QApplication(sys.argv)
    calcMax = CalcMax()
    calcMax.show()
    sys.exit(app.exec_())


main()