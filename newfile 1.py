from tkinter import *

# Create window
root = Tk()
root.title("MATHEMATICAL CALCULATOR (MC)")
root.geometry("350x500")
root.resizable(False, False)

# Entry field
entry = Entry(root, font=("Arial", 20), bd=10, relief=RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Function to display values
def click(value):
    entry.insert(END, value)


# Function to clear screen
def clear():
    entry.delete(0, END)


# Function to evaluate expression
def calculate():
    try:
        expression = entry.get().replace("^", "**")
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")


# Function to close calculator
def off():
    root.destroy()


# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
    ('^', 5, 0), ('(', 5, 1), (')', 5, 2), ('=', 5, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=8, height=3,
               command=calculate).grid(row=row, column=col)
    else:
        Button(root, text=text, width=8, height=3,
               command=lambda t=text: click(t)).grid(row=row, column=col)

# Clear button
Button(root, text="C", width=17, height=3,
       command=clear).grid(row=6, column=0, columnspan=2)

# OFF button
Button(root, text="OFF", width=17, height=3,
       command=off).grid(row=6, column=2, columnspan=2)

root.mainloop()