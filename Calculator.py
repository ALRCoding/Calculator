from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create entry widget for displaying calculations
        self.display = Entry(master, width=20, font=('Arial', 16), justify=RIGHT)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons for calculator
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)
        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)
        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('=', 4, 2)
        self.create_button('+', 4, 3)
        self.create_button('C', 5, 0)
        self.create_button('CE', 5, 1)

    def create_button(self, text, row, column):
        button = Button(self.master, text=text, width=5, height=2, font=('Arial', 16),
                        command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=2, pady=2)

    def button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, END)
                self.display.insert(END, result)
            except:
                self.display.delete(0, END)
                self.display.insert(END, 'Error')
        elif text == 'C':
            self.display.delete(0, END)
        elif text == 'CE':
            self.display.delete(len(self.display.get())-1, END)
        else:
            self.display.insert(END, text)

root = Tk()
calc = Calculator(root)
root.mainloop()
