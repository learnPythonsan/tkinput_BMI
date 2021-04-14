import tkinter as tk
from PIL import ImageTk, Image
from tkinter import StringVar
from tkinter import ttk
# 柯老師到此一遊
# 柯老師到此一遊 ver 2

def compute():
    global entry1 #身高
    global entry2 #體重
    global label1Str
    #BMI值計算公式:    BMI = 體重(公斤) / 身高2(公尺2)
    #52(公斤)/1.552 ( 公尺2 )= 21.6
    tall=entry1.get()
    weight=entry2.get()
    ans = int(weight)/((int(tall)/100)*(int(tall)/100))
    label1Str.set(ans)


win = tk.Tk()
win.wm_title("BMI轉換")                 # 設定抬頭名稱
win.minsize(width=800, height=400)   # 320,200
win.maxsize(width=800, height=400)  # 1024 768
win.resizable(width=False, height=False) # 是否可以改變視窗大小
################################################################
title1=tk.Label(win,text="請輸入身高:") # 新增名稱標籤
title1.place(x=0,y=0)

entry1=tk.Entry(win)
entry1.place(x=0,y=30)

title2=tk.Label(win,text="請輸入體重:") # 新增名稱標籤
title2.place(x=0,y=60)

entry2=tk.Entry(win)
entry2.place(x=0,y=90)

btn1 =tk.Button(win,text="輸入完確定",command=compute)
btn1.place(x=0,y=120)

title3=tk.Label(win,text="BMI為:") # 新增名稱標籤
title3.place(x=0,y=150)
label1Str=StringVar()
title4=tk.Label(win,text="...",textvariable=label1Str) # 新增名稱標籤
title4.place(x=0,y=180)


win.mainloop()
