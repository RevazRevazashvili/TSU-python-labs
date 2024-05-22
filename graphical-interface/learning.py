import tkinter as tk

########### N1 ##############
# window = tk.Tk()
#
# label = tk.Label(text="python rocks!")
# label.pack()
#
# window.mainloop()


######## N2 ##########
# window = tk.Tk()
#
# txt = tk.Text()
# txt.pack()
# button1 = tk.Button(text="delete character")
# button2 = tk.Button(text="clear all")
# button3 = tk.Button(text="get value")
#
# def delchar(event):
#     txt.delete('1.0')
#
#
# def clearchar(event):
#     txt.delete('1.0', tk.END)
#
#
# def getval(event):
#     label1 = tk.Label()
#     label1 = tk.Label(text=txt.get('1.0', tk.END))
#     label1.pack()
#
#
# button1.bind("<Button-1>", delchar)
# button2.bind("<Button-1>", clearchar)
# button3.bind("<Button-1>", getval)
#
# button1.pack()
# button2.pack()
# button3.pack()
# window.mainloop()


########### N3 #############

# window = tk.Tk()
#
# frame_a = tk.Frame()
# frame_b = tk.Frame()
#
# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()
#
# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()
#
# frame_a.pack()
# frame_b.pack()
#
# window.mainloop()


############ N4 ###############

# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
#
# window = tk.Tk()
#
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()
#
# window.mainloop()


############ N5 #############
# window = tk.Tk()
#
# en = tk.Entry()
# en.pack()
#
# en.insert("end", "Hello World")
#
# window.mainloop()


############### N6 ###############

# window = tk.Tk()
#
# frame1 = tk.Frame(master=window, height=100, bg="red")
# frame1.pack(fill=tk.X)
#
# frame2 = tk.Frame(master=window, height=50, bg="yellow")
# frame2.pack(fill=tk.X)
#
# frame3 = tk.Frame(master=window, height=25, bg="blue")
# frame3.pack(fill=tk.BOTH)
#
# window.mainloop()



############### N7 ###############

# window = tk.Tk()
#
# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()
#
# window.mainloop()


############### N8 ###############


# window = tk.Tk()
#
# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()
#
# window.mainloop()


############### N8 ###############


# window = tk.Tk()
#
# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
#
#     for j in range(0, 3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)
#
# window.mainloop()


############### N9 ###############

# window = tk.Tk()
#
# # border_effects = {
# #     "flat": tk.FLAT,
# #     "sunken": tk.SUNKEN,
# #     "raised": tk.RAISED,
# #     "groove": tk.GROOVE,
# #     "ridge": tk.RIDGE,
# # }
#
# lab_list = ['name', 'surname', 'address', 'city', 'state', 'country']
#
# inputs = tk.Frame(window, bg="green", relief=tk.SUNKEN)
# inputs.pack(padx=10, pady=10)
#
# label = tk.Frame(inputs)
# label.pack()
#
# counter = 0
# for i, label_text in enumerate(lab_list):
#     lab = tk.Label(label, text=f"{label_text}: ", width=10, height=3, padx=5, pady=5)
#     ent = tk.Text(label, width=10, height=1, padx=5, pady=5)
#     lab.grid(column=0, row=i, sticky="w")
#     ent.grid(column=1, row=i, sticky="w")
#
# buttons = tk.Frame(window, bg="green")
# buttons.pack(padx=10, pady=10, side=tk.RIGHT)
#
# but1 = tk.Button(buttons, text="clear")
# but1.grid(column=0, row=0)
#
# but2 = tk.Button(buttons, text="submit")
# but2.grid(column=1, row=0)
#
# window.mainloop()


############### N10 ###############

# window = tk.Tk()
#
# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)
#
# # Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)
#
# window.mainloop()


############### N11 ###############


# import sys
# from PyQt5.QtWidgets import QApplication, QPushButton
#
# app = QApplication(sys.argv)
#
# window = QPushButton("Push Me")
# window.show()
#
# app.exec()

############### N12 ###############

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
#
# app = QApplication(sys.argv)
#
# window = QMainWindow()
# window.show()
#
# # Start the event loop.
# app.exec()

############### N13 ###############

# import sys
#
# from PyQt5.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDateEdit,
#     QDateTimeEdit,
#     QDial,
#     QDoubleSpinBox,
#     QFontComboBox,
#     QLabel,
#     QLCDNumber,
#     QLineEdit,
#     QMainWindow,
#     QProgressBar,
#     QPushButton,
#     QRadioButton,
#     QSlider,
#     QSpinBox,
#     QTimeEdit,
#     QVBoxLayout,
#     QWidget,
# )
#
# # Subclass QMainWindow to customize your application's main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Widgets App")
#
#         layout = QVBoxLayout()
#         widgets = [
#             QCheckBox,
#             QComboBox,
#             QDateEdit,
#             QDateTimeEdit,
#             QDial,
#             QDoubleSpinBox,
#             QFontComboBox,
#             QLCDNumber,
#             QLabel,
#             QLineEdit,
#             QProgressBar,
#             QPushButton,
#             QRadioButton,
#             QSlider,
#             QSpinBox,
#             QTimeEdit,
#         ]
#
#         for w in widgets:
#             layout.addWidget(w())
#
#         widget = QWidget()
#         widget.setLayout(layout)
#
#         # Set the central widget of the Window. Widget will expand
#         # to take up all the space in the window by default.
#         self.setCentralWidget(widget)
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()

############### N14 ###############
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
# from PyQt5 import QtWidgets
# import sys
#
#
# def window():
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     win.setGeometry(300, 300, 300, 300)
#     win.setWindowTitle('Graphical Interface')
#
#     label = QLabel(win)
#     label.setText("Hello there")
#     label.move(10, 10)
#
#     label1 = QLabel(win)
#     label1.setText("how are you?")
#     label1.move(100, 50)
#
#     win2 = QMainWindow()
#     win2.setGeometry(400, 400, 300, 300)
#     win2.setWindowTitle('Graphical Interface1')
#
#     win.show()
#     win2.show()
#
#     sys.exit(app.exec_())
#
# window()

# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
# import sys
#
# def clicked():
#     print("clicked")
# def window():
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     win.setGeometry(300, 300, 500, 500)
#     win.setWindowTitle("Graphical Interface")
#
#     label = QLabel(win)
#     label.setText("Welcome to Graphical Interface")
#     label.move(30, 30)
#     label.adjustSize()
#
#     b1 = QPushButton("click me", win)
#     b1.move(50, 50)
#     b1.clicked.connect(clicked)
#     # b1.connect(clicked())
#
#
#     win.show()
#     sys.exit(app.exec_())
#
# window()

from PyQt5 import QtWidgets
from PyQt5.uic.properties import QtGui

# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
# import sys
#
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(300, 300, 500, 500)
#         self.setWindowTitle("Graphical Interface")
#         self.initUI()
#
#     def initUI(self):
#         self.label = QLabel(self)
#         self.label.setText("Welcome to Graphical Interface")
#         self.label.move(30, 30)
#         self.label.adjustSize()
#
#         self.b1 = QPushButton("click me", self)
#         self.b1.move(50, 50)
#         self.b1.clicked.connect(self.clicked)
#
#     def clicked(self):
#         self.label.setText("you pressed the button")
#         self.label.adjustSize()
#
# def window():
#     app = QApplication(sys.argv)
#     win = MyWindow()
#
#     win.show()
#     sys.exit(app.exec_())
#
# window()


# import sqlite3
#
# with sqlite3.connect('ko.db') as conn:
#   cursor = conn.cursor()
#
# comm = """ select * from Student """
# Stud_List = cursor.execute(comm).fetchall()
# # Stud_List = cursor.execute(comm).fetchone()
# print(Stud_List)

