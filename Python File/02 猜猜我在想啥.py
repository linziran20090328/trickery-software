#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time         :       2021/8/30 14:46
# @Author       :       林子然
# @File         :       02 猜猜我在想啥.py
# @Software     :       Pycharm

import tkinter as tk
from tkinter.messagebox import showerror

root = tk.Tk()
root.geometry('300x400')



tk.Label(root, text='猜猜我在想什么', width=20, font=('宋体', 16)).pack()
text = tk.Text(root)
text.pack(fill=tk.X)
text.bind('<Return>', lambda event: showerror('错误', '猜错咯'))
tk.Button(root, text='提交', command=lambda: showerror('错误', '猜错咯')).pack()

def on_exit():
    showerror('Error', '此路不通')


root.protocol('WM_DELETE_WINDOW', on_exit)
root.mainloop()