# -*- coding: utf-8 -*-
from robot import Robot
from tkinter import *
from PIL import Image, ImageTk

speaker = Robot("Speaker", "vi")

def Speaker(info):
    global speaker
    if info != "" and info != None:
        speaker.RobotRead(info)

def main():
    
    RoBot = Tk()
    RoBot.title("Robot text to speech")
    
    myimg = ImageTk.PhotoImage(Image.open('aaa.png'))
    Label(RoBot, image=myimg).grid(row=0, column=0)
    Label(RoBot, text=u"Nhập một chuỗi để tôi đọc cho bạn!", fg="#003300").grid(row=1, column=0)
    
    data = Entry(RoBot, width = 100)
    data.grid(row=2, column=0)

    Button(RoBot, text=u"Đọc văn bản", padx=75, pady=25, command=lambda: Speaker(data.get()), fg="white", bg="#009900").grid(row=3, column=0)

    RoBot.mainloop()


if __name__ == "__main__":
    main()