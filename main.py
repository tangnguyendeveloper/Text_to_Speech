# -*- coding: utf-8 -*-
from tkinter.tix import Tree
import robot as r
import speech_recognition as sr

recognizer = sr.Recognizer()

lib = {
    u"anh tên gì": u"Dạ anh tên Tạng",
    u"đẹp trai không": u"Dạ em thấy thầy rất tự tin nên suy ra thầy siêu đẹp trai ạ!",
    u"Thầy đẹp trai không": u"Dạ em thấy thầy rất tự tin nên suy ra thầy siêu đẹp trai ạ!"
}

def get_text_from_mic():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(u"Hãy nói gì đó... tong 4 giấy!")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("____")

    try:
        print("...")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="vi-VN"
            )
        return text

    except Exception as ex:
        print(ex)
        return ""

#honey.RobotReadFile("test.txt")

print("Hãy nói:", u"chào em")

while True:
    text = get_text_from_mic()
    print(text)
    
    if text in [u"chào em"]:
        honey = r.Robot("Honey", "vi")
        honey.RobotRead(u"Dạ em đây ạ! Anh cần gì hông nè!")
        text = get_text_from_mic()
        print(text)
        if text == "":
            honey = r.Robot("Honey", "vi")
            honey.RobotRead(u"Dạ anh ơi! Sao Em hổng nghe anh nói thế!")
        else:
            try:
                honey = r.Robot("Honey", "vi")
                m = lib[text]
                honey.RobotRead(m)
                #honey.RobotRead(u"Dạ xin lỗi anh nha! cái này em hổng biết gòi!")
            except:
                honey = r.Robot("Honey", "vi")
                honey.RobotRead(u"Dạ xin lỗi anh nha! cái này em hổng biết gòi!")
    print(text)


