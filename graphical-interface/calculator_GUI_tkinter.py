# გამოსადეგი ბმულები

# https://realpython.com/python-gui-tkinter/

import tkinter as tk

window = tk.Tk()

# window.geometry('500x500')

window_frame = tk.Frame(window, bg="#4169E1")

input_frame = tk.Frame(master=window_frame)
first_line_attrs = tk.Frame(master=window_frame)
second_line_attrs = tk.Frame(master=window_frame)
third_line_attrs = tk.Frame(master=window_frame)
fourth_line_attrs = tk.Frame(master=window_frame)
fifth_line_attrs = tk.Frame(master=window_frame)
sixth_line_attrs = tk.Frame(master=window_frame)

input_txt = tk.Entry(master=input_frame, width=50, justify='right')
percent = tk.Button(master=first_line_attrs, text="%", width=5, height=2, bg='green', fg='white')
CE = tk.Button(master=first_line_attrs, text="CE", width=5, height=2,)
C = tk.Button(master=first_line_attrs, text="C", width=5, height=2,)
del_one = tk.Button(master=first_line_attrs, text="del", width=5, height=2, bg='#8B0000', fg='white')

oneByX = tk.Button(master=second_line_attrs, text="1/x", width=5, height=2,)
xSquare = tk.Button(master=second_line_attrs, text="x^2", width=5, height=2,)
sqrt = tk.Button(master=second_line_attrs, text="sqrt(x)", width=5, height=2,)
divide = tk.Button(master=second_line_attrs, text="/", width=5, height=2,)

seven = tk.Button(master=third_line_attrs, text="7", width=5, height=2,)
eight = tk.Button(master=third_line_attrs, text="8", width=5, height=2,)
nine = tk.Button(master=third_line_attrs, text="9", width=5, height=2,)
mult = tk.Button(master=third_line_attrs, text="*", width=5, height=2,)

four = tk.Button(master=fourth_line_attrs, text="4", width=5, height=2,)
five = tk.Button(master=fourth_line_attrs, text="5", width=5, height=2,)
six = tk.Button(master=fourth_line_attrs, text="6", width=5, height=2,)
minus = tk.Button(master=fourth_line_attrs, text="-", width=5, height=2,)

one = tk.Button(master=fifth_line_attrs, text="1", width=5, height=2,)
two = tk.Button(master=fifth_line_attrs, text="2", width=5, height=2,)
three = tk.Button(master=fifth_line_attrs, text="3", width=5, height=2,)
plus = tk.Button(master=fifth_line_attrs, text="+", width=5, height=2,)

plusminus = tk.Button(master=sixth_line_attrs, text="+-", width=5, height=2,)
zero = tk.Button(master=sixth_line_attrs, text="0", width=5, height=2,)
dot = tk.Button(master=sixth_line_attrs, text=".", width=5, height=2,)
equal = tk.Button(master=sixth_line_attrs, text="=", width=5, height=2, bg='#E9967A', fg='white')

input_txt.pack()
input_txt.insert("0", "0")

input_frame.pack()

first_line_attrs.pack()

percent.pack(side=tk.LEFT)
CE.pack(side=tk.LEFT)
C.pack(side=tk.LEFT)
del_one.pack(side=tk.LEFT)

second_line_attrs.pack()

oneByX.pack(side=tk.LEFT)
xSquare.pack(side=tk.LEFT)
sqrt.pack(side=tk.LEFT)
divide.pack(side=tk.LEFT)

third_line_attrs.pack()

seven.pack(side=tk.LEFT)
eight.pack(side=tk.LEFT)
nine.pack(side=tk.LEFT)
mult.pack(side=tk.LEFT)

fourth_line_attrs.pack()

four.pack(side=tk.LEFT)
five.pack(side=tk.LEFT)
six.pack(side=tk.LEFT)
minus.pack(side=tk.LEFT)

fifth_line_attrs.pack()

one.pack(side=tk.LEFT)
two.pack(side=tk.LEFT)
three.pack(side=tk.LEFT)
plus.pack(side=tk.LEFT)

sixth_line_attrs.pack()

plusminus.pack(side=tk.LEFT)
zero.pack(side=tk.LEFT)
dot.pack(side=tk.LEFT)
equal.pack(side=tk.LEFT)

window_frame.pack()

def oneb(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "1")
    else:
        input_txt.insert(tk.END, "1")

def twob(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "2")
    else:
        input_txt.insert(tk.END, "2")

def threeb(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "3")
    else:
        input_txt.insert(tk.END, "3")

def fourb(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "4")
    else:
        input_txt.insert(tk.END, "4")

def fifth(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "5")
    else:
        input_txt.insert(tk.END, "5")

def sixth(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "6")
    else:
        input_txt.insert(tk.END, "6")

def seventh(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "7")
    else:
        input_txt.insert(tk.END, "7")

def eighth(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "8")
    else:
        input_txt.insert(tk.END, "8")

def nineth(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "9")
    else:
        input_txt.insert(tk.END, "9")

def zeroth(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "0")
    else:
        input_txt.insert(tk.END, "0")

def percenct(event):
    if input_txt.get() == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, "0")
    else:
        num = int(input_txt.get())
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, str(num/100))

def CEb(event):
    input_txt.delete(0, tk.END)
    input_txt.insert(tk.END, "0")

def Cb(event):
    input_txt.delete(0, tk.END)
    input_txt.insert(tk.END, "0")

def del_oneb(event):
    n = input_txt.get()
    n = n[:-1]
    input_txt.delete(0, tk.END)
    input_txt.insert(tk.END, n)
    if not n:
        input_txt.insert(tk.END, "0")

def onebyXb(event):
    num = input_txt.get()
    if num.isnumeric():
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, str(1/int(num)))
    else:
        print("error")

def xSquareb(event):
    num = input_txt.get()
    if num.isnumeric():
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, str(int(num)**2))
    else:
        print("error")

def sqrtbb(event):
    num = input_txt.get()
    if num.isnumeric():
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, str(int(num)**0.5))
    else:
        print("error")

def divideb(event):
    num = input_txt.get()
    num = num.split()
    if num[-1].isnumeric():
        num[-1] = " / "
        input_txt.insert(tk.END, str(''.join(num)))

def multb(event):
    num = input_txt.get()
    num = num.split()
    if num[-1].isnumeric():
        num[-1] = " * "
        input_txt.insert(tk.END, str(''.join(num)))

def plusbb(event):
    num = input_txt.get()
    num = num.split()
    if num[-1].isnumeric():
        num[-1] = " + "
        input_txt.insert(tk.END, str(''.join(num)))

def minusb(event):
    num = input_txt.get()
    num = num.split()
    if num[-1].isnumeric():
        num[-1] = " - "
        input_txt.insert(tk.END, str(''.join(num)))

def equalb(event):
    num = input_txt.get()
    num = num.split()
    input_txt.delete(0, tk.END)
    match num[1]:
        case "+":
            input_txt.insert(tk.END, str(int(num[0])+int(num[2])))
        case "-":
            input_txt.insert(tk.END, str(int(num[0])-int(num[2])))
        case "/":
            input_txt.insert(tk.END, str(int(num[0])/int(num[2])))
        case "*":
            input_txt.insert(tk.END, str(int(num[0])*int(num[2])))

one.bind('<Button-1>', oneb)
two.bind('<Button-1>', twob)
three.bind('<Button-1>', threeb)
four.bind('<Button-1>', fourb)
five.bind('<Button-1>', fifth)
six.bind('<Button-1>', sixth)
seven.bind('<Button-1>', seventh)
eight.bind('<Button-1>', eighth)
nine.bind('<Button-1>', nineth)
zero.bind('<Button-1>', zeroth)
percent.bind('<Button-1>', percenct)
CE.bind('<Button-1>', CEb)
C.bind('<Button-1>', Cb)
del_one.bind('<Button-1>', del_oneb)
oneByX.bind('<Button-1>', onebyXb)
xSquare.bind('<Button-1>', xSquareb)
sqrt.bind('<Button-1>', sqrtbb)
divide.bind('<Button-1>', divideb)
mult.bind('<Button-1>', multb)
plus.bind('<Button-1>', plusbb)
minus.bind('<Button-1>', minusb)
equal.bind('<Button-1>', equalb)


window.mainloop()

