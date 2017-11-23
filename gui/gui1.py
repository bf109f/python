# _*_ coding:utf-8 _*_
from tkinter import *
# import tkFileDialog  # python2
# import tkMessageBox  # python2
import os
import fnmatch
# from ScrolledText import ScrolledText  # python2
import tkinter.messagebox
import tkinter.filedialog
import tkinter.scrolledtext


def search():
    """
    搜索
    :return:
    """
    entkw = ent.get()
    enttype = ent2.get()
    if not (entkw and enttype):
        tkinter.messagebox.showerror('错误', '输入为空')
        return
    path = tkinter.filedialog.askdirectory()
    listbox.delete(0, END)
    fnlist = os.walk(path)
    for i, dirs, files in fnlist:
        # i 当前正在遍历的文件夹 dirs 当前文件夹下的所有子文件夹 files 当前文件夹下的所有文件
        for n in fnmatch.filter(files, enttype):  # 实现列表的字符过滤，返回符合匹配模式的字符列表（筛选后缀）
            fn = '%s/%s' % (i, n)
            fn = fn.replace('\\', '/')
            f = open(fn)
            if entkw in f.read():
                listbox.insert(END, fn)
            f.close()


def openfile(event):
    """
    打开文件
    :return:
    """
    fn = listbox.get(listbox.curselection())
    str_1 = open(fn).read()
    editwindow = Tk()
    editwindow.title(fn)
    edittext = tkinter.scrolledtext(editwindow, width=120, height=60)  # 多行文本框
    edittext.grid()
    edittext.insert(INSERT, str_1)
    editwindow.mainloop()


# 实例化对象(窗口)
root = Tk()
root.title('文件搜索工具')
# 设置窗口大小
root.geometry('+500+300')  # + 设置坐标
# root.geometry('300x200')  # 设置大小
Label(root, text='关键字：').grid()
ent = Entry(root)  # 创建控件(单选框)
ent.grid(row=0, column=1)  # 显示、布局 1、表示第二个位置
Label(root, text='文件类型：').grid(row=0, column=2)
ent2 = Entry(root)
ent2.grid(row=0, column=3)
btn = Button(root, text='搜 索', command=search)
btn.grid(row=0, column=4)
listbox = Listbox(root, width='80')
listbox.bind('<Double-Button-1>', openfile)
listbox.grid(row=1, columnspan=5)
# 显示窗口（一直循环执行）
root.mainloop()