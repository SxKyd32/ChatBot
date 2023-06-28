from tkinter import *
import tkinter as tk
import requests
import time
# import tkinter.font as tf

# 图灵机器人
apiUrl = 'http://www.tuling123.com/openapi/api'
key = '73b1deee524b4162b4a26922b3e1addd'
userid = '妹妹'

def main():
    # 发送消息
    def send_msg():
        str_msg = "我:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        txt_msg_list.insert(END,
                          # 文本
                          str_msg,
                          # 颜色
                          'greencolor')
        txt_msg_list.insert(END,
                          # 文本
                          txt_msg.get('0.0', END))
        get_response(txt_msg.get('0.0', END))
        txt_msg.delete('0.0', END)

    # 接收消息
    def get_response(message):
        data = {
            'key': key,
            'info': message,
            'userid': userid,
        }

        try:
            rs = requests.post(apiUrl, data=data).json()
            str_msg_bot = "妮可:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
            txt_msg_list.insert(END,
                              # 文本
                              str_msg_bot,
                              # 颜色
                              'purplecolor')
            txt_msg_list.insert(END,
                              # 文本
                              rs['text'] + '\n',)
            # print('回复:%s' % rs['text'])
            return rs['text']
        except:
            return 0

    # 取消信息
    def cancel_msg():
        txt_msg.delete('0.0', END)

    # 发送消息事件
    def send_msg_event(event):
        if event.keysym == 'Up':
            send_msg()

    # 创建窗口
    window_chat = tk.Tk()
    window_chat.title('和妮可聊天吧！')

    # 创建frame容器
    frm_lt = Frame(width=500, height=320, bg='white')
    frm_lc = Frame(width=500, height=150, bg='white')
    frm_lb = Frame(width=500, height=30)
    frm_rt = Frame(width=375, height=500)

    # 创建控件
    txt_msg_list = Text(frm_lt)
    txt_msg_list.tag_config('greencolor', foreground='#008C00')  # 创建绿色tag
    txt_msg_list.tag_config('purplecolor', foreground='#BA55D3')  # 创建紫色tag
    txt_msg = Text(frm_lc)
    txt_msg.bind("<KeyPress-Up>", send_msg_event)
    btn_send = Button(frm_lb, text='发 送', width=10, command=send_msg)
    btn_cancel = Button(frm_lb, text='取 消', width=10, command=cancel_msg)
    # img_info = PhotoImage(file="D:\Cherchez\JetBrains\Pycharm_Projects\ChatBot\ico.gif")
    img_info = PhotoImage(file="ico.gif")
    label_image = Label(frm_rt, image=img_info)
    label_image.image = img_info

    # 窗口布局
    frm_lt.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
    frm_lc.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
    frm_lb.grid(row=2, column=0, columnspan=2)
    frm_rt.grid(row=0, column=2, rowspan=3, padx=2, pady=3)

    # 固定大小
    frm_lt.grid_propagate(0)
    frm_lc.grid_propagate(0)
    frm_lb.grid_propagate(0)
    frm_rt.grid_propagate(0)

    btn_send.grid(row=2, column=0)
    btn_cancel.grid(row=2, column=1)
    label_image.grid()
    txt_msg_list.grid()
    txt_msg.grid()

    window_chat.mainloop()
