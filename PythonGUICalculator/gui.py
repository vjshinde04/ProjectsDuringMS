
import tkinter as tk

window = tk.Tk()

# greeting = tk.Label(text="Welcome to Calculator")
# greeting.pack()
global operationFlag
global firstNum
global secondNum
operationFlag = 0

def FuncButtonClick(number):
    current = d.get()
    d.delete(0, tk.END)
    d.insert(0, str(current) + str(number))

def FuncClear():
    d.delete(0, tk.END)

def FuncAdd():
    num = d.get()
    firstNum = int(num)
    d.delete(0, tk.END)
    operationFlag = 1

def FuncEqual():
    currentNum = d.get()
    secondNum = int(currentNum)
    d.delete(0, tk.END)
    if operationFlag == 1:
        d.insert(0, firstNum + secondNum)

d = tk.Entry(window)
d.grid(row=0, columnspan=4)

from tkinter.ttk import *
buttonStyle = Style()
buttonStyle.configure('bs', font=('Ariel', 10), background='black', foreground='white')

button0 = tk.Button(window, text="0", padx=22, pady=20, command=lambda: FuncButtonClick(0))
button0.grid(row=5,column=1)
button1 = tk.Button(window, text="1", padx=22, pady=20, command=lambda: FuncButtonClick(1))
button1.grid(row=4,column=0)
button2 = tk.Button(window, text="2", padx=22, pady=20, command=lambda: FuncButtonClick(2))
button2.grid(row=4,column=1)
button3 = tk.Button(window, text="3", padx=22, pady=20, command=lambda: FuncButtonClick(3))
button3.grid(row=4,column=2)
button4 = tk.Button(window, text="4", padx=22, pady=20, command=lambda: FuncButtonClick(4))
button4.grid(row=3,column=0)
button5 = tk.Button(window, text="5", padx=22, pady=20, command=lambda: FuncButtonClick(5))
button5.grid(row=3,column=1)
button6 = tk.Button(window, text="6", padx=22, pady=20, command=lambda: FuncButtonClick(6))
button6.grid(row=3,column=2)
button7 = tk.Button(window, text="7", padx=22, pady=20, command=lambda: FuncButtonClick(7))
button7.grid(row=2,column=0)
button8 = tk.Button(window, text="8", padx=22, pady=20, command=lambda: FuncButtonClick(8))
button8.grid(row=2,column=1)
button9 = tk.Button(window, text="9", padx=22, pady=20, command=lambda: FuncButtonClick(9))
button9.grid(row=2,column=2)

buttonDec = tk.Button(window, text=".", padx=24, pady=20, command=lambda: FuncButtonClick("."))
buttonDec.grid(row=5,column=2)
buttonSciSwitch = tk.Button(window, text="~", padx=21, pady=20)
buttonSciSwitch.grid(row=5,column=0)

buttonEqual = tk.Button(window, text="=", padx=19.5, pady=20, command=FuncEqual)
buttonEqual.grid(row=5,column=3)
buttonAdd = tk.Button(window, text="+", padx=21, pady=20, command=FuncAdd)
buttonAdd.grid(row=4,column=3)
buttonSub = tk.Button(window, text="-", padx=22, pady=20)
buttonSub.grid(row=3,column=3)
buttonMul = tk.Button(window, text="x", padx=22, pady=20)
buttonMul.grid(row=2,column=3)
buttonDiv = tk.Button(window, text="/", padx=22, pady=20)
buttonDiv.grid(row=1,column=3)

buttonPercent = tk.Button(window, text="%", padx=20, pady=20)
buttonPercent.grid(row=1,column=2)
buttonClear = tk.Button(window, text="<", padx=21, pady=20, command=FuncClear)
buttonClear.grid(row=1,column=1)
buttonAllClear = tk.Button(window, text="AC", padx=18, pady=20)
buttonAllClear.grid(row=1,column=0)









window.mainloop()

