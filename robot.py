# -*- coding: utf-8 -*-
from gtts import gTTS 
import os

class Robot():
    def __init__(self, pname, planguage):
        self.__name = pname
        self.__language = planguage

    def __del__(self):
        os.remove(self.__name + ".mp3")
        del self.__name
        del self.__language

    @property
    def name(self):
        return self.__name

    def RobotRead(self, StringText):
        myrobot = gTTS(text=StringText+u"", lang=self.__language, slow=False)  
        myrobot.save(self.__name+".mp3") 
        os.system("mpg321 "+self.__name+".mp3")

    def RobotReadFile(self, NameFile):
        f = open(NameFile, mode='r', encoding='utf-8')
        mytext = str(f.read()) +u""
        f.close()
        myrobot = gTTS(text=mytext, lang=self.__language, slow=False)  
        myrobot.save(self.__name+".mp3") 
        os.system("mpg321 "+self.__name+".mp3")


