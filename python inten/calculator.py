""" a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = a+b
d = a-b
e = a*b
f = a/b
g = a//b
h = a%b
print("addition value is : ",c)
print("subraction value is : ",d)
print("multiplication value is : ",e)
print("divition value is : ",f)
print("qution value is : ",g)
print("mod value is : ",h) """

import tkinter

part = tkinter.Tk()
part.title("Calculator")


expression = ""

# Create functions
def add (value):
    global expression
    expression += value
    l_result.config(text = expression)

def clear():
    global expression
    expression = ""
    l_result.config(text = expression)


def calc():
    global expression
    result = " "
    if expression != " ":
        try:
            result = eval(expression)
        except:
            result = "ERROR"
            expression = ""
    l_result.config(text = result)


l_result = tkinter.Label(part, text=" ")
l_result.grid(row = 0,column=0 , columnspan=5)

button1 = tkinter.Button(part, text="1",command=lambda: add("1"))
button1.grid(row=1,column=0)

button2 = tkinter.Button(part, text="2",command=lambda: add("2"))
button2.grid(row=1,column=1)

button3 = tkinter.Button(part, text="3",command=lambda: add("3"))
button3.grid(row=1,column=2)

button_divide = tkinter.Button(part, text="/",command=lambda: add("/"))
button_divide.grid(row=1,column=3)



button4 = tkinter.Button(part, text="4",command=lambda: add("4"))
button4.grid(row=2,column=0)

button5 = tkinter.Button(part, text="5",command=lambda: add("5"))
button5.grid(row=2,column=1)

button6 = tkinter.Button(part, text="6",command=lambda: add("6"))
button6.grid(row=2,column=2)

button_mul = tkinter.Button(part, text="*",command=lambda: add("*"))
button_mul.grid(row=2,column=3)



button7 = tkinter.Button(part, text="7",command=lambda: add("7"))
button7.grid(row=3,column=0)

button8 = tkinter.Button(part, text="8",command=lambda: add("8"))
button8.grid(row=3,column=1)

button9 = tkinter.Button(part, text="9",command=lambda: add("9"))
button9.grid(row=3,column=2)

button_sub = tkinter.Button(part, text="-",command=lambda: add("-"))
button_sub.grid(row=3,column=3)



button_clear = tkinter.Button(part, text="C",command=lambda: clear())
button_clear.grid(row=4,column=0)

button0 = tkinter.Button(part, text="0",command=lambda: add("0"))
button0.grid(row=4,column=1)

button_dot = tkinter.Button(part, text=".",command=lambda: add("."))
button_dot.grid(row=4,column=2)

button_add = tkinter.Button(part, text="+",command=lambda: add("+"))
button_add.grid(row=4,column=3)



button_equals =tkinter.Button(part, text="=", width=16, command=lambda: calc())
button_equals.grid(row=5, column=0, columnspan=4)



part.mainloop()