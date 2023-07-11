from tkinter import *
import math

expression = ""

def input_number(number, equation):
    global expression
    expression = expression + str(number)
    equation.set(expression)

def clear_input_field(equation):
    global expression
    expression = ""
    equation.set("Enter the expression")

def evaluate(equation):
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
    except ZeroDivisionError:
        equation.set("Error")
        expression = ""
    except ValueError:
        equation.set("Error")
        expression = ""
    except OverflowError:
        equation.set("Error")
        expression = ""
    except SyntaxError:
        equation.set("Error")
        expression = ""

def sqrt_c():
    global expression
    re = str(eval(expression) ** 0.5)
    expression = re

def square_c():
    global expression
    re = str(eval(expression) ** 2)
    expression = re

def back_input(equation):
    global expression
    l = len(expression)
    expression = expression[:l - 1]
    equation.set(expression)

root = Tk()
root.title("Calculator")
root.geometry("305x352")
equation = StringVar()
input_field = Entry(root, textvariable=equation, bd=5, selectborderwidth=50, width=40)
input_field.place(width=100, height=100)
input_field.grid(columnspan=100, ipadx=10, ipady=10)
_1 = Button(root, text='1', fg='white', bg='black', bd=0, command=lambda: input_number(1, equation), height=3,
            width=10).grid(row=5, column=0)
_2 = Button(root, text='2', fg='white', bg='black', bd=0, command=lambda: input_number(2, equation), height=3,
            width=10).grid(row=5, column=1)
_3 = Button(root, text='3', fg='white', bg='black', bd=0, command=lambda: input_number(3, equation), height=3,
            width=10).grid(row=5, column=2)
_4 = Button(root, text='4', fg='white', bg='black', bd=0, command=lambda: input_number(4, equation), height=3,
            width=10).grid(row=4, column=0)
_5 = Button(root, text='5', fg='white', bg='black', bd=0, command=lambda: input_number(5, equation), height=3,
            width=10).grid(row=4, column=1)
_6 = Button(root, text='6', fg='white', bg='black', bd=0, command=lambda: input_number(6, equation), height=3,
            width=10).grid(row=4, column=2)
_7 = Button(root, text='7', fg='white', bg='black', bd=0, command=lambda: input_number(7, equation), height=3,
            width=10).grid(row=3, column=0)
_8 = Button(root, text='8', fg='white', bg='black', bd=0, command=lambda: input_number(8, equation), height=3,
            width=10).grid(row=3, column=1)
_9 = Button(root, text='9', fg='white', bg='black', bd=0, command=lambda: input_number(9, equation), height=3,
            width=10).grid(row=3, column=2)
_0 = Button(root, text='0', fg='white', bg='black', bd=0, command=lambda: input_number(0, equation), height=3,
            width=10).grid(row=6, column=1)
plus = Button(root, text='+', fg='white', bg='black', bd=0, command=lambda: input_number('+', equation), height=3,
            width=10).grid(row=5, column=3)
minus = Button(root, text='-', fg='white', bg='black', bd=0, command=lambda: input_number('-', equation), height=3,
            width=10).grid(row=4, column=3)
mul = Button(root, text='*', fg='white', bg='black', bd=0, command=lambda: input_number('*', equation), height=3,
            width=10).grid(row=3, column=3)
div = Button(root, text='/', fg='white', bg='black', bd=0, command=lambda: input_number('/', equation), height=3,
            width=10).grid(row=6, column=3)
eq = Button(root, text='=', fg='white', bg='black', bd=0, command=lambda: evaluate(equation), height=3, width=10).grid(
            row=6, column=2)
clc = Button(root, text='Clear', fg='black', bg='white', bd=0, command=lambda: clear_input_field(equation), height=3,
            width=20).grid(columnspan=2, row=1, column=0)
dot = Button(root, text='.', fg='white', bg='black', bd=0, command=lambda: input_number('.', equation), height=3,
            width=10).grid(row=6, column=0)
back = Button(root, text='DEL', fg='black', bg='white', bd=0, command=lambda: back_input(equation), height=3,
            width=20).grid(columnspan=2, row=1, column=2)
bf = Button(root, text='(', fg='white', bg='black', bd=0, command=lambda: input_number('(', equation), height=3,
            width=10).grid(row=2, column=2)
bb = Button(root, text=')', fg='white', bg='black', bd=0, command=lambda: input_number(')', equation), height=3,
            width=10).grid(row=2, column=3)
sqrt = Button(root, text='sqrt', fg='white', bg='black', bd=0, command=lambda: sqrt_c(), height=3, width=10).grid(row=2,
             column=0)
square = Button(root, text='square', fg='white', bg='black', bd=0, command=lambda: square_c(), height=3, width=10).grid(
                row=2, column=1)
root.mainloop()