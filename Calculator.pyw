from tkinter import *

class GUI:

    def __init__(self,parent):
        self.parent = parent
        self.initUI()
        self.process = ""
        self.operations = ["+","-","×","/"]

    def initUI(self):
        self.display = Label(height = 3, width = 42, bg =  "white", anchor = CENTER)
        self.display.place(x = 5, y = 7)
        self.ce_button = Button(text = "CE", width = 7,command = self.clear)
        self.ce_button.place(x = 5, y = 70)
        self.c_button = Button(text = "C", width = 7, command = self.clear)
        self.c_button.place(x = 85, y = 70)
        self.delete_button = Button(text = "⇽", width = 7, command = self.delete)
        self.delete_button.place(x = 165, y = 70)
        self.divide_button = Button(text = "÷", width = 7, command = self.divide)
        self.divide_button.place(x = 245, y = 70)
        self.seven_button = Button(text = "7", width = 7, command = self.seven)
        self.seven_button.place(x = 5, y = 110)
        self.eight_button = Button(text = "8", width = 7, command = self.eight)
        self.eight_button.place(x = 85, y = 110)
        self.nine_button = Button(text = "9", width = 7, command = self.nine)
        self.nine_button.place(x = 165, y = 110)
        self.multiply_button = Button(text = "×", width = 7, command = self.multiply)
        self.multiply_button.place(x = 245, y = 110)
        self.four_button = Button(text = "4", width = 7, command = self.four)
        self.four_button.place(x = 5, y = 150)
        self.five_button = Button(text = "5", width = 7, command = self.five)
        self.five_button.place(x = 85, y = 150)
        self.six_button = Button(text = "6", width = 7, command = self.six)
        self.six_button.place(x = 165, y = 150)
        self.minus_button = Button(text = "–", width = 7, command = self.minus)
        self.minus_button.place(x = 245, y = 150)
        self.one_button = Button(text = "1", width = 7, command = self.one)
        self.one_button.place(x = 5, y = 190)
        self.two_button = Button(text = "2", width = 7, command = self.two)
        self.two_button.place(x = 85, y = 190)
        self.three_button = Button(text = "3", width = 7, command = self.three)
        self.three_button.place(x = 165, y = 190)
        self.plus_button = Button(text = "+", width = 7, command = self.plus)
        self.plus_button.place(x = 245, y =190)
        self.change_button = Button(text = "±", width = 7, command = self.change)
        self.change_button.place(x = 5, y = 230)
        self.zero_button = Button(text = "0", width = 7, command = self.zero)
        self.zero_button.place(x = 85, y = 230)
        self.coma_button = Button(text = ".", width = 7, command = self.coma)
        self.coma_button.place(x = 165, y = 230)
        self.equal_button = Button(text = "=", width = 7, command = self.equal)
        self.equal_button.place(x = 245, y = 230)

    def zero(self):
        self.process += "0"
        self.display.config(text = self.process)

    def one(self):
        self.process += "1"
        self.display.config(text = self.process)

    def two(self):
        self.process += "2"
        self.display.config(text = self.process)

    def three(self):
        self.process += "3"
        self.display.config(text = self.process)

    def four(self):
        self.process += "4"
        self.display.config(text = self.process)

    def five(self):
        self.process += "5"
        self.display.config(text = self.process)

    def six(self):
        self.process += "6"
        self.display.config(text = self.process)

    def seven(self):
        self.process += "7"
        self.display.config(text = self.process)

    def eight(self):
        self.process += "8"
        self.display.config(text = self.process)

    def nine(self):
        self.process += "9"
        self.display.config(text = self.process)

    def plus(self):
        self.process += "+"
        self.display.config(text = self.process)

    def minus(self):
        self.process += "-"
        self.display.config(text = self.process)

    def clear(self):
        self.process = ""
        self.display.config(text = 0)

    def ce(self):
        pass

    def divide(self):
        self.process += "/"
        self.display.config(text = self.process)

    def multiply(self):
        self.process += "×"
        self.display.config(text = self.process)

    def coma(self):
        self.process += "."
        self.display.config(text = self.process)

    def delete(self):
        self.pro = list(self.process)
        self.pro.pop(-1)
        self.process = "".join(self.pro)
        self.display.config(text = self.process)

    def change(self):
        try:
            self.changed = int(self.process) * (-1)
            self.process = str(self.changed)
            self.display.config(text=self.process)

        except ValueError as hata:
            self.display.config(text = "Syntax Error")
            self.process = ""
        else:
            pass

    def equal(self):
        self.pro = list(self.process)
        for i in range(len(self.pro)):
            if self.pro[i] == "×":
               self.pro[i] = "*"
        self.process = "".join(self.pro)
        self.process = str(eval((self.process)))
        if "." in self.process:
            self.pro = self.process.split(".")
            if self.pro[1] == "0":
                self.process = self.pro[0]
        self.display.config(text = self.process)

def main():
    root = Tk()
    root.title("Calculator")
    root.geometry("310x290")
    app = GUI(root)
    root.mainloop()

main()
