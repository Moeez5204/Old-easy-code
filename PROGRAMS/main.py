# import tkinter libraries
import tkinter as tk
from tkinter import messagebox

# create root window
root = tk.Tk()

# display basic window
root.title("Calculator")
root.geometry("500x300")

# label for the display
lbl = tk.Label(root)
lbl.pack(fill=tk.BOTH, expand=True)

# calculator label
calc_label = tk.Label(text="Calculator: ")



# This function is used for updating the result on
# the label and performing operations as soon as any
# button is pressed
def btn_click(num):
    global expression
    if (expression == "0"):
        expression = ""
        expression = expression + str(num)
    else:
        expression = expression + str(num)
    lbl.configure(text=expression)



# Function to evaluate the final expression
def btn_equal_click():
    global expression
    result = str(eval(expression))
    lbl.configure(text=result)

def clear():
    global expression
    expression = "0"
    lbl.configure(text= expression)




# Empty expression variable
expression = "0"

# Buttons present in the calculator
btn_1 = tk.Button(root, text="1", command=lambda: btn_click(1))
btn_2 = tk.Button(root, text="2", command=lambda: btn_click(2))
btn_3 = tk.Button(root, text="3", command=lambda: btn_click(3))
btn_4 = tk.Button(root, text="4", command=lambda: btn_click(4))
btn_5 = tk.Button(root, text="5", command=lambda: btn_click(5))
btn_6 = tk.Button(root, text="6", command=lambda: btn_click(6))
btn_7 = tk.Button(root, text="7", command=lambda: btn_click(7))
btn_8 = tk.Button(root, text="8", command=lambda: btn_click(8))
btn_9 = tk.Button(root, text="9", command=lambda: btn_click(9))
btn_0 = tk.Button(root, text="0", command=lambda: btn_click(0))

btn_divide = tk.Button(root, text="/", command=lambda: btn_click("/"))
btn_multiply = tk.Button(root, text="*", command=lambda: btn_click("*"))
btn_plus = tk.Button(root, text="+", command=lambda: btn_click("+"))
btn_minus = tk.Button(root, text="-", command=lambda: btn_click("-"))
btn_equal = tk.Button(root, text="=", command=btn_equal_click)

btn_clear = tk.Button(root, text="Clear", command=lambda: clear())

# Placing the buttons on the screen

calc_label.place(relx=0.3, rely=0.3)
lbl.place(relx=0.46, rely= 0.3)

btn_1.place(relx=0.05, rely=0.5)
btn_2.place(relx=0.2, rely=0.5)
btn_3.place(relx=0.35, rely=0.5)
btn_plus.place(relx=0.5, rely=0.5)

btn_4.place(relx=0.05, rely=0.6)
btn_5.place(relx=0.2, rely=0.6)
btn_6.place(relx=0.35, rely=0.6)
btn_minus.place(relx=0.5, rely=0.6)

btn_7.place(relx=0.05, rely=0.7)
btn_8.place(relx=0.2, rely=0.7)
btn_9.place(relx=0.35, rely=0.7)
btn_multiply.place(relx=0.5, rely=0.7)

btn_0.place(relx=0.2, rely=0.8)
btn_equal.place(relx=0.35, rely=0.8)
btn_divide.place(relx=0.5, rely=0.8)

btn_clear.place(relx=0.05, rely=0.8)

# endlessly loop main window
root.mainloop()