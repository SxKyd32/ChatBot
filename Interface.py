# from tkinter import *
import tkinter as tk
import tkinter.messagebox
import pickle
import ChatWindow
# import time
# import os

window = tk.Tk()
window.title('欢迎使用wyz的聊天机器人，来和妮可聊天吧！')
window.geometry('800x540')

# 主页图片
canvas = tk.Canvas(window, bg='white', height=320, width=718)
# image_file = tk.PhotoImage(file='D:\Cherchez\JetBrains\Pycharm_Projects\ChatBot\welcome.gif')
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# 用户信息
label_usr_name = tk.Label(
             # 文本
             text='用 户 ：',
             # 字体
             font=('行楷', 15, 'bold')
             ).place(x=250, y=340)
    # tk.Label(window, text='用 户 ：').place(x=250, y=340)

# 用户输入框
var_usr_name = tk.StringVar() # 用于存用户名
# var_usr_name.set('在此输入用户名(邮箱)')  # 默认值
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=340, y=343)

# 密码信息
label_usr_pwd = tk.Label(
             # 文本
             text='密 码 ：',
             # 字体
             font=('行楷', 15, 'bold')
             ).place(x=250, y=380)
    # tk.Label(window, text='密 码 ：').place(x=250, y=380)

# 密码输入框
var_usr_pwd = tk.StringVar() # 用于存密码
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=340, y=383)

# 关闭当前页面，跳转至聊天界面
def jump_to_chat():
    global window
    window.destroy()
    ChatWindow.main()

# 登陆功能
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 存放数据
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin':'admin'}   # 管理员身份
            pickle.dump(usrs_info, usr_file)

    # 判断输入的用户名及密码是否正确
    if usr_name in usrs_info:   # 判断用户名是否存在
        if usr_pwd == usrs_info[usr_name]:  # 判断密码是否正确
            tk.messagebox.showinfo(title='欢迎！', message='好久不见，' + usr_name + '！')
            jump_to_chat()  # 跳转至聊天页面
        else:
            tk.messagebox.showerror(title='出错了！', message='好像不对呢，再检查一下吧。')
    elif usr_name == '':  # 用户名为空
        tk.messagebox.showerror(title='出错了！', message='好像啥也没写呢，请输入用户名和密码哦！')
    else:   # 询问是否要注册
        is_sign_up = tk.messagebox.askyesno(title='欢迎！', message='好像没有账号呢，要不要注册一个呢？')
        if is_sign_up:
            usr_sign_up()   # 跳转至注册界面

# 注册功能
def usr_sign_up():
    def sign_to_wyz_infosave():
        nn = new_name.get()
        np = new_pwd.get()
        npc = new_pwd_confirm.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npc:   # 两次密码输入不同
            tk.messagebox.showerror(title='注册失败了！', message='两次密码输入要相同哦，重新输入一遍吧！')
        elif nn in exist_usr_info:  # 用户名查重
            tk.messagebox.showerror(title='注册失败了！', message='这个用户名已经被使用了，换一个试试。')
        else:   # 写入新用户信息到usr_file
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo(title='注册成功！', message='恭喜你注册成功！')
            window_sign_up.destroy()

    def sign_up_return():
        window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册一个账号吧！')

    new_name = tk.StringVar()   # 用户
    new_name.set('example@python.com')
    label_new_name = tk.Label(window_sign_up, text='用 户 :').place(x=30, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()    # 密码
    label_new_pwd = tk.Label(window_sign_up, text='密 码 :').place(x=30, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_new_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()    # 确认密码
    label_new_pwd_confirm = tk.Label(window_sign_up, text='确 认 密 码 :').place(x=30, y=90)
    entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_new_pwd_confirm.place(x=150, y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up, text=' 立  即  注  册 ', command=sign_to_wyz_infosave)
    btn_confirm_sign_up.place(x=60, y=140)

    btn_sign_up_return = tk.Button(window_sign_up, text=' 返  回  主  页 ', command=sign_up_return)
    btn_sign_up_return.place(x=190, y=140)

def usr_exit():
    window.destroy()

# 登录按钮
btn_login = tk.Button(window, text=' 现  在  登  录 ', command=usr_login)
btn_login.place(x=170, y=460)

# 注册按钮
btn_sign_up = tk.Button(window, text=' 注  册  一  个 ', command=usr_sign_up)
btn_sign_up.place(x=360, y=460)

# 退出按钮
btn_exit = tk.Button(window, text=' 下  次  再  见 ', command=usr_exit)
btn_exit.place(x=550, y=460)

window.mainloop()
