#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time         :       2021/8/30 14:34
# @Author       :       林子然
# @File         :       01 你是一个傻狍子.py
# @Software     :       Pycharm

import threading
import tkinter as tk
import random


def show():
    root = tk.Tk()
    root.geometry(f'215x40+{random.randint(0, root.winfo_screenwidth())}+{random.randint(0, root.winfo_screenwidth())}')
    tk.Label(root, text='你是一个傻狍子', bg='green', font=('宋体', 24), pady=10).pack()
    root.mainloop()

while True:
    threading.Thread(target=show).start()




