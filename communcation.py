# -*- coding: utf-8 -*-
# from tkinter import *  # 将tkinter导入到工程中
from tkinter import PhotoImage, Frame, Button, Label, Scale
import serial  # 导入库
import time
import tkinter
import cv2
from PIL import Image, ImageTk
serialPort = "COM8"
baudRate = 9600
ser = serial.Serial(port=serialPort, baudrate=baudRate, timeout=1)
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))
time.sleep(4)

'''acc_left为左边车轮油门的中间参数，
   用于转向时，减低左轮的油门值，形成左右速差'''
acc_left = 0
acc_right = 0  # 右边车轮油门的中间参数

root = tkinter.Tk()  # 创建窗体对象
root.wm_title('4w_motor Control')  # 设置窗口标题

curWidth = 1050  # 窗口宽度
curHight = 500  # 窗口度

# 获取屏幕宽度和高度
scn_w, scn_h = root.maxsize()
# print(scn_w, scn_h)

# 计算中心坐标
cen_x = (scn_w - curWidth) / 2
cen_y = (scn_h - curHight) / 2
# print(cen_x, cen_y)

# 设置窗口初始大小和位置
size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)  # 注意这里的x是英文字母x
root.geometry(size_xy)  # 设置窗口大小


def forward():
    '''直线前进'''
    acc_value = scale_accelerator.get()
    ser.write((str(acc_value) + "w").encode())


def reverse():
    '''直线后退'''
    acc_value = scale_accelerator.get()
    ser.write((str(acc_value) + "x").encode())


def leftTurn():
    '''原地左转弯'''
    acc_value = scale_accelerator.get()  # 获取油门值
    ser.write((str(acc_value) + "a").encode())


def rightTurn():
    '''原地右转弯'''
    acc_value = scale_accelerator.get()
    ser.write((str(acc_value) + "d").encode())


def brake():
    '''刹车'''
    acc_value = scale_accelerator.get()
    ser.write((str(acc_value) + "s").encode())


def forward_left():
    '''朝左前方转向行进'''
    acc_value = scale_accelerator.get()  # 获取油门值
    ser.write((str(acc_value) + "q").encode())


def forward_right():
    '''朝右前方转向行进'''
    acc_value = scale_accelerator.get()  # 获取油门值
    ser.write((str(acc_value) + "e").encode())


def reverse_left():
    '''朝左后方转向倒车'''
    acc_value = scale_accelerator.get()  # 获取油门值
    ser.write((str(acc_value) + "z").encode())


def reverse_right():
    '''朝右后方转向倒车'''
    acc_value = scale_accelerator.get()  # 获取油门值
    ser.write((str(acc_value) + "c").encode())


def callback(event):
    char = event.char
    print(char)
    acc_value = scale_accelerator.get()
    ser.write((str(acc_value) + char).encode())


frame = Frame(root, width=500, height=500)
frame.bind("<Key>", callback)
frame.focus_set()
frame.pack(side="left", padx=10, pady=10)

'''定义前进、后退、原地左转、原地右转、刹车插图的对象'''
top_img = PhotoImage(file='./control_images/top.png')
down_img = PhotoImage(file='./control_images/down.png')
left_img = PhotoImage(file='./control_images/left.png')
right_img = PhotoImage(file='./control_images/right.png')
stop_img = PhotoImage(file='./control_images/stop.png')
'''定义左前、右前、左后、右后行进插图的对象'''
top_left_img = PhotoImage(file='./control_images/left_top.png')
top_right_img = PhotoImage(file='./control_images/right_top.png')
down_left_img = PhotoImage(file='./control_images/left_down.png')
down_right_img = PhotoImage(file='./control_images/right_down.png')

'''定义按钮'''

Button(frame, text='top_left', bd=10, image=top_left_img, command=forward_left).grid(row=1, column=1)
Button(frame, text='forward', bd=10, image=top_img, command=forward).grid(row=1, column=2)
Button(frame, text='top_right', bd=10, image=top_right_img, command=forward_right).grid(row=1, column=3)

Button(frame, text='left', bd=10, image=left_img, command=leftTurn).grid(row=2, column=1)
Button(frame, text='brake', bd=10, image=stop_img, command=brake).grid(row=2, column=2)
Button(frame, text='right', bd=10, image=right_img, command=rightTurn).grid(row=2, column=3)

Button(frame, text='down_left', bd=10, image=down_left_img, command=reverse_left).grid(row=3, column=1)

Button(frame, text='reverse', bd=10, image=down_img, command=reverse).grid(row=3, column=2)

Button(frame, text='down_right', bd=10, image=down_right_img, command=reverse_right).grid(row=3, column=3)


def contrarotate():
    '''定义逆时针旋转'''
    acc_value = scale_accelerator.get()
    ser.write((str(acc_value) + "h").encode())


def clockwise_rotation():
    '''定义顺时针旋转'''
    acc_value = scale_accelerator.get()
    ser.write((str(acc_value) + "j").encode())


def rotate_by_right_down():
    '''绕右后轮旋转'''
    acc_value = scale_accelerator.get()
    ser.write((str(acc_value) + "k").encode())


def rotate_by_down_center():
    '''绕后轮中心旋转'''
    acc_value = scale_accelerator.get()
    ser.write((str(acc_value) + "l").encode())


'''定义逆时针旋转、顺时针旋转、绕右后轮旋转、绕后轮中心旋转行进插图的对象'''
contrarotate_img = PhotoImage(file='./control_images/contrarotate.png')
clockwise_rotation_img = PhotoImage(file='./control_images/clockwise_rotation.png')
rotate_by_right_down_img = PhotoImage(file='./control_images/rotate_by_right_down.png')
rotate_by_down_center_img = PhotoImage(file='./control_images/rotate_by_down_center.png')
'''定义按钮'''
rotate_frame = Frame(root, background="red", width=200, height=600)
rotate_frame.pack(side="right", padx=10, pady=10)
Button(rotate_frame, text='contrarotate', bd=10, image=contrarotate_img, command=contrarotate).grid(row=1)
Button(rotate_frame, text='clockwise_rotation', bd=10, image=clockwise_rotation_img, command=clockwise_rotation).grid(row=2)
Button(rotate_frame, text='rotate_by_right_down', bd=10, image=rotate_by_right_down_img, command=rotate_by_right_down).grid(
    row=3)
Button(rotate_frame, text='rotate_by_down_center', bd=10, image=rotate_by_down_center_img, command=rotate_by_down_center).grid(row=4)

'''定义标签'''
label1 = Label(root,
               text='speed',
               fg='red',
               font=24,
               )
label1.place(x=800, y=450)

'''根据scale滑动条的值，调整油门大小'''


def movetriangle(event):
    if event.keysym == 'Up':
        scale_accelerator.set(scale_accelerator.get() + 10)
    elif event.keysym == 'Down':
        scale_accelerator.set(scale_accelerator.get() - 10)


'''定义scale滑动条'''
scale_accelerator = Scale(root,
                          # label='accelerator', # 设置显示的标签
                          from_=100,  # 设置最大最小值
                          to=0,
                          resolution=10,  # 设置步距值
                          # orient=VERTICAL,  # 如果我们想设置成垂直方向改怎么办呢？直接缺省这个属性就可以啦，默认就是垂直
                          # show=0,    # 隐藏滑动条的值
                          # variable=value_a, # 绑定Scale的值为我们所用
                          activebackground='red',
                          length=350,
                          width=30,  # 设置Scale的宽度,默认是16。
                          sliderlength=50,  # 滑块的大小。默认值是30
                          bd=10,  # 设置Scale控件边框宽度
                          tickinterval=20,  # 显示刻度，并定义刻度的粒度
                          troughcolor='red',  # 设置滑动槽的背景颜色

                          )
scale_accelerator.place(x=750, y=50)
scale_accelerator.bind_all('<KeyPress-Up>', movetriangle)
scale_accelerator.bind_all('<KeyPress-Down>', movetriangle)


# 创建一个TK界面
video = cv2.VideoCapture(0)


def imshow():
    global video
    global root
    global image
    res, img = video.read()

    if res == True:
        # 将adarray转化为image
        img = Image.fromarray(img)
        # 显示图片到label
        img = ImageTk.PhotoImage(img)
        image.image = img
        image['image'] = img
    # 创建一个定时器，每10ms进入一次函数
    root.after(10, imshow)


# 创建label标签
video_Frame = tkinter.Frame(root).pack()
image = tkinter.Label(video_Frame, text='video ', width=320, height=320)
image.place(x=400, y=100, width=320, height=320)

imshow()

root.mainloop()

# 释放video资源
video.release()
