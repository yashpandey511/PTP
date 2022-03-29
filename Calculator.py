
from tkinter import *

window = Tk()

window.geometry("225x230")
window.title("Calculator")

ent = Entry(window, width=16, borderwidth=3, relief=RIDGE)
ent.grid(pady=10, row=0, sticky="w", padx=15)


def delete():
    a = ent.get()
    ent.delete(first=len(a)-1, last="end")


def clear():
    ent.delete(0, "end")


def result():
    if ent.get() == "":
        pass
    elif ent.get()[0] == "0":
        ent.delete(0, "end")
    else:
        res = ent.get()
        res = eval(res)
        clear()
        ent.insert("end", res)

clean = Button(window, text="C", width=2, command=clear, relief=RIDGE)
clean.grid(row=0, sticky="w", padx=125)
nine = Button(window, text="9", width=2, command=lambda: ent.insert("end", "9"), borderwidth=3,  relief=RIDGE)
nine.grid(row=1, sticky="w", padx=15)
eight = Button(window, text="8", width=2, command=lambda: ent.insert("end", "8"), borderwidth=3,  relief=RIDGE)
eight.grid(row=1, sticky="w", padx=45)
seven = Button(window, text="7", width=2, command=lambda: ent.insert("end", "7"), borderwidth=3,  relief=RIDGE)
seven.grid(row=1, sticky="w", padx=75)
plus = Button(window, text="+", width=2, command=lambda: ent.insert("end", "+"), borderwidth=3,  relief=RIDGE)
plus.grid(row=1, sticky="e", padx=125)
six = Button(text="6", width=2, command=lambda: ent.insert("end", "6"), borderwidth=3, relief=RIDGE)
six.grid(row=2, sticky="w", padx=15, pady=5)
five = Button(text="5", width=2, command=lambda: ent.insert("end", "5"), borderwidth=3, relief=RIDGE)
five.grid(row=2, sticky="w", padx=45, pady=5)
four = Button(window, text="4", width=2, command=lambda: ent.insert("end", "4"), borderwidth=3, relief=RIDGE)
four.grid(row=2, sticky="w", padx=75, pady=5)
minus = Button(window, text="-", width=2, command=lambda: ent.insert("end", "-"), borderwidth=3, relief=RIDGE)
minus.grid(row=2, sticky="e", padx=125, pady=5)
three = Button(text="3", width=2, command=lambda: ent.insert("end", "3"), borderwidth=3, relief=RIDGE)
three.grid(row=3, sticky="w", padx=15, pady=5)
two = Button(text="2", width=2, command=lambda: ent.insert("end", "2"), borderwidth=3, relief=RIDGE)
two.grid(row=3, sticky="w", padx=45, pady=5)
one = Button(window, text="1", width=2, command=lambda: ent.insert("end", "1"), borderwidth=3, relief=RIDGE)
one.grid(row=3, sticky="w", padx=75, pady=5)
multiply = Button(window, text="*", width=2, command=lambda: ent.insert("end", "*"), borderwidth=3, relief=RIDGE)
multiply.grid(row=3, sticky="e", padx=125, pady=5)
zero = Button(text="0", width=2, command=lambda: ent.insert("end", "0"), borderwidth=3, relief=RIDGE)
zero.grid(row=4, sticky="w", padx=15, pady=5)
double_zero = Button(text="00", width=2, command=lambda: ent.insert("end", "00"), borderwidth=3, relief=RIDGE)
double_zero.grid(row=4, sticky="w", padx=45, pady=5)
dot = Button(window, text=".", width=2, command=lambda: ent.insert("end", "."), borderwidth=3, relief=RIDGE)
dot.grid(row=4, sticky="w", padx=75, pady=5)
divide = Button(window, text="/", width=2, command=lambda: ent.insert("end", "/"), borderwidth=3, relief=RIDGE)
divide.grid(row=4, sticky="e", padx=125, pady=5)
equal = Button(window, text="=", width=10, command=result, borderwidth=3, relief=RIDGE)
equal.grid(row=5, sticky="w", padx=15, pady=5)
percent = Button(window, text="%", width=2, command=lambda: ent.insert("end", "%"), borderwidth=3, relief=RIDGE)
percent.grid(row=5, sticky="e", padx=125, pady=5)
delete = Button(window, text="del", width=2, command=delete, borderwidth=3, relief=RIDGE)
delete.grid(row=5, sticky="w", padx=98, pady=5)

window.mainloop()
