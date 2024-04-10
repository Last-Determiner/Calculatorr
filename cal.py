
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Calculator by Maghzian")
        MainWindow.setFixedSize(370, 420)
        MainWindow.setStyleSheet("QWidget {"
                                 "    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 1, fx: 0.5, fy: 0.5, stop: 0 rgba(50, 50, 50, 255), stop: 1 rgba(0, 0, 0, 255));"  # Use radial gradient for background
                                 "    border: 2px solid White; /* Yellow border */"
                                 "}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Number 7
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(20, 80, 51, 51))
        self.style_buttom(self.seven)
        self.seven.setObjectName("seven")
        self.seven.clicked.connect(lambda : self.clicked_num("7"))
        self.seven.clicked.connect(lambda: self.change_button_color(self.seven))
        # Number 8
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(90, 80, 51, 51))
        self.style_buttom(self.eight)
        self.eight.setObjectName("eight")
        self.eight.clicked.connect(lambda: self.clicked_num("8"))
        self.eight.clicked.connect(lambda: self.change_button_color(self.eight))
        # Number 9
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(160, 80, 51, 51))
        self.style_buttom(self.nine)
        self.nine.setObjectName("nine")
        self.nine.clicked.connect(lambda: self.clicked_num("9"))
        self.nine.clicked.connect(lambda: self.change_button_color(self.nine))
        # Dividing operation button
        self.div = QtWidgets.QPushButton(self.centralwidget)
        self.div.setGeometry(QtCore.QRect(230, 80, 51, 51))
        self.style_buttom(self.div)
        self.div.setObjectName("div")
        self.div.clicked.connect(lambda: self.clicked_func("/", self.div))
        self.div.clicked.connect(lambda: self.change_button_color(self.div))
        # Number 6
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(160, 150, 51, 51))
        self.style_buttom(self.six)
        self.six.setObjectName("six")
        self.six.clicked.connect(lambda: self.clicked_num("6"))
        self.six.clicked.connect(lambda: self.change_button_color(self.six))
        # Number 5
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(90, 150, 51, 51))
        self.style_buttom(self.five)
        self.five.setObjectName("five")
        self.five.clicked.connect(lambda: self.clicked_num("5"))
        self.five.clicked.connect(lambda: self.change_button_color(self.five))
        # Number 4
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(20, 150, 51, 51))
        self.style_buttom(self.four)
        self.four.setObjectName("four")
        self.four.clicked.connect(lambda: self.clicked_num("4"))
        self.four.clicked.connect(lambda: self.change_button_color(self.four))
        # multiplying operation key
        self.mult = QtWidgets.QPushButton(self.centralwidget)
        self.mult.setGeometry(QtCore.QRect(230, 150, 51, 51))
        self.style_buttom(self.mult)
        self.mult.setObjectName("mult")
        self.mult.clicked.connect(lambda: self.clicked_func("*", self.mult))
        self.mult.clicked.connect(lambda: self.change_button_color(self.mult))
        # point
        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(160, 290, 51, 51))
        self.style_buttom(self.point)
        self.point.setObjectName("point")
        self.point.clicked.connect(lambda: self.clicked_twice(".", self.point))
        self.point.clicked.connect(lambda: self.change_button_color(self.point))
        # all clear
        self.ac = QtWidgets.QPushButton(self.centralwidget)
        self.ac.setGeometry(QtCore.QRect(20, 290, 51, 51))
        self.style_buttom(self.ac)
        self.ac.setObjectName("ac")
        self.ac.clicked.connect(self.allclear)
        self.ac.clicked.connect(lambda: self.change_button_color(self.ac))
        # Number 3
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(160, 220, 51, 51))
        self.style_buttom(self.three)
        self.three.setObjectName("three")
        self.three.clicked.connect(lambda: self.clicked_num("3"))
        self.three.clicked.connect(lambda: self.change_button_color(self.three))
        # Number 0
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(90, 290, 51, 51))
        self.style_buttom(self.zero)
        self.zero.setObjectName("zero")
        self.zero.clicked.connect(lambda: self.clicked_num("0"))
        self.zero.clicked.connect(lambda: self.change_button_color(self.zero))
        # Number 2
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(90, 220, 51, 51))
        self.style_buttom(self.two)
        self.two.setObjectName("two")
        self.two.clicked.connect(lambda: self.clicked_num("2"))
        self.two.clicked.connect(lambda: self.change_button_color(self.two))
        # Number 1
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(20, 220, 51, 51))
        self.style_buttom(self.one)
        self.one.setObjectName("one")
        self.one.clicked.connect(lambda: self.clicked_num("1"))
        self.one.clicked.connect(lambda: self.change_button_color(self.one))
        # Adding up operation key
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(230, 290, 51, 51))
        self.style_buttom(self.plus)
        self.plus.setObjectName("plus")
        self.plus.clicked.connect(lambda: self.clicked_func("+", self.plus))
        self.plus.clicked.connect(lambda: self.change_button_color(self.plus))
        # Subtracting operation key
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(230, 220, 51, 51))
        self.style_buttom(self.minus)
        self.minus.setObjectName("minus")
        self.minus.clicked.connect(lambda: self.clicked_func("-", self.minus))
        self.minus.clicked.connect(lambda: self.change_button_color(self.minus))
        # Precentage operation key
        self.precent = QtWidgets.QPushButton(self.centralwidget)
        self.precent.setGeometry(QtCore.QRect(300, 220, 51, 51))
        self.style_buttom(self.precent)
        self.precent.setObjectName("precent")
        self.precent.clicked.connect(self.percentage)
        self.precent.clicked.connect(lambda: self.change_button_color(self.precent))
        #Backspace key
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(300, 290, 51, 51))
        self.style_buttom(self.back)
        self.back.setObjectName("back")
        self.back.clicked.connect(self.back_delete)
        self.back.clicked.connect(lambda: self.change_button_color(self.back))
        #To power operation key
        self.power = QtWidgets.QPushButton(self.centralwidget)
        self.power.setGeometry(QtCore.QRect(300, 150, 51, 51))
        self.style_buttom(self.power)
        self.power.setObjectName("power")
        self.power.clicked.connect(lambda: self.clicked_once("**",self.power))
        self.power.clicked.connect(lambda: self.change_button_color(self.power))
        #Equal key
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(300, 80, 51, 51))
        self.style_buttom(self.equal)
        self.equal.setObjectName("equal")
        self.equal.clicked.connect(self.equal_end)
        self.equal.clicked.connect(lambda: self.change_button_color(self.equal))
        # Label of Creadit
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 350, 331, 31))
        self.label.setStyleSheet("QLabel {"
                                 "    font-family: \"Times New Roman\", Times, serif;"
                                 "    color: #990000; "
                                 "    border: 2px solid #990000; /* Add a border around the label */"
                                 "    border-radius: 10px; /* Add border radius for rounded corners */"
                                 "    padding: 5px; /* Add padding */"
                                 "    background-color: rgba(255, 255, 255, 150); /* Semi-transparent white background */"
                                 "    font-size: 13pt; /* Font size of 15 points */"
                                 "}"
                                 "")
        self.label.setObjectName("label")
        # Box / textEdit
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 331, 61))
        self.textEdit.setStyleSheet("QTextEdit {"
                                    "    background-color: rgba(255, 255, 255, 255); /* Semi-transparent white background */"
                                    "    color: #000000; /* Black text */"
                                    "    font-size: 13pt; /* Font size of 10 points */"
                                    "    border-radius: 10px; /* Add border radius for rounded corners */"
                                    "    padding: 5px; /* Add padding */"
                                    "}"
                                    "")
        self.textEdit.setObjectName("textEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # Change key styles here with one edit
    def style_buttom(self, button):
        button.setStyleSheet("QPushButton {\n"
                             "    width: 100px;\n"
                             "    height: 100px;\n"
                             "    border-radius: 20px; /* Adjust border-radius for a slightly rounder button */\n"
                             "    background-color: white;\n"
                             "    border: 2px solid black;\n"
                             "    color: black;\n"
                             "    font-size: 16px;\n"
                             "    font-weight: bold;\n"
                             "}\n"
                             "")
    # Change button color and revert back after a short delay
    def change_button_color(self, button):
        original_color = button.palette().button().color()
        new_color = QtGui.QColor(255, 165, 0)  # Change to orange color
        button.setStyleSheet(
            f"background-color: {new_color.name()}; border: 2px solid black; color: black; font-size: 16px; font-weight: bold; border-radius: 20px;")
        QtCore.QTimer.singleShot(200, lambda: button.setStyleSheet(
            f"background-color: {original_color.name()}; border: 2px solid black; color: black; font-size: 16px; font-weight: bold; border-radius: 20px;"))

    #================================== Functions section ====================================================
    def clicked_num(self,num):
        text = self.textEdit.textCursor()
        text.insertText(num)


    def percentage(self):
        text = self.textEdit.toPlainText()
        if text:
            result = eval(text)
            answer = result / 100
            self.textEdit.setText(str(answer))
    def clicked_func(self,func,button):
        cursor = self.textEdit.textCursor()
        text = self.textEdit.toPlainText()
        operators = ["+", "-", "*", "/"]
        if text[-1] in operators:
            return
        else:
            cursor.insertText(func)

    def clicked_twice(self, func, button):
        text = self.textEdit.toPlainText()
        operators = ["+", "-", "*", "/"]
        current_operand = ''
        for op in reversed(text):
            if op in operators:
                break
            current_operand = op + current_operand

        if '.' not in current_operand:
            cursor = self.textEdit.textCursor()
            cursor.insertText(func)

    def clicked_once(self, func, button):
        text = self.textEdit.textCursor()
        text.insertText(func)
        button.clicked.disconnect()

    def equal_end(self):
        all = self.textEdit.toPlainText()
        answer =eval(all)
        self.textEdit.setText(str(answer))
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
    def back_delete(self):
        all_text = self.textEdit.toPlainText()
        all_text = all_text[:-1]
        self.textEdit.setText(all_text)
    def allclear(self):
        self.textEdit.setText("")
        # self.point.clicked.connect(lambda: self.clicked_once(".", self.point))
        self.power.clicked.connect(lambda: self.clicked_once("**", self.power))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator by Maghzian"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.div.setText(_translate("MainWindow", "÷"))
        self.six.setText(_translate("MainWindow", "6"))
        self.five.setText(_translate("MainWindow", "5"))
        self.four.setText(_translate("MainWindow", "4"))
        self.mult.setText(_translate("MainWindow", "*"))
        self.point.setText(_translate("MainWindow", "."))
        self.ac.setText(_translate("MainWindow", "AC"))
        self.three.setText(_translate("MainWindow", "3"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.two.setText(_translate("MainWindow", "2"))
        self.one.setText(_translate("MainWindow", "1"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.precent.setText(_translate("MainWindow", "%"))
        self.back.setText(_translate("MainWindow", "⌫"))
        self.power.setText(_translate("MainWindow", "^"))
        self.equal.setText(_translate("MainWindow", "=    "))
        self.label.setText(_translate("MainWindow", "    by Mohammadreza Maghzian for a project "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
