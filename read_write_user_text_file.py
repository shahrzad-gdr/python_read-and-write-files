"""
+---------------------------------------------------------------+
+    How to read and write in a text file, using Python         +
+    In this project we let the user to select text file to     +
+     read, and select the output file                          +
+---------------------------------------------------------------+
"""
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

read_path = filedialog.askopenfilename()

number_list = []
with open(read_path) as read_file:
    content = read_file.readlines()
    for item in content:
        # print(item.strip())     # output: print each line in text file
        number = int(item.strip())
        number_list.append(number)
        print(number)           # output: print each number with integer type




write_path = filedialog.asksaveasfilename(filetypes=(("Text Files", "*.txt"),))
with open(write_path, 'w') as write_file:
    for item in number_list:
        for i in range(0,item):
            write_file.write('*')
        write_file.write('\n')

