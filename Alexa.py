from matplotlib.pyplot import text
from numpy import size
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from breezypythongui import EasyFrame
from tkinter import *

top = Tk()
top.geometry("650x500")
# text = Text(top, height=15, font=('Times New Roman', 17, 'bold'))
# text.insert(INSERT,"WELCOME TO ALEXA 2.0")
alexa_gui = Label(top, bg='purple', text="WELCOME TO ALEXA 2.0").place(x=220, y=200)
text = Text(top, height=15, font=('Times New Roman', 40, 'bold'))
top.configure(bg='black')
#font = ('Helvetica 20 bold').pack(pady=20)

top.after(4000, lambda: top.destroy())


class VoiceBot():
    BOT_NAME = 'alexa'
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def takeCommand(self):
        self.talk("Hello welcome to alexa two point o. How can i help you")
        listener = self.listener

        try:
            with sr.Microphone() as source:
                #label = Message(top, textvariable='Listening', relief=RAISED)
                print('Listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if self.BOT_NAME in command:
                    command = command.replace(self.BOT_NAME, '').strip()

        except:
            pass

        return command

    def runAlexa(self):
        try:
            command = self.takeCommand()
            print(f'User: {command}')

            if 'play' in command:
                song = command.replace('play', '')
                self.talk('playing'+song)
                self.talk('playing')
                pywhatkit.playonyt(song)

            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                self.talk('Current time is'+time)

            elif 'tell about' in command:
                person = command.replace('tell about', '')
                info = wikipedia.summary(person, 2)
                print(info)
                self.talk(info)

            elif 'what is your age' in command:
                self.talk('I am twenty five years old')

            elif 'joke' in command:
                self.talk(pyjokes.get_joke())

            elif 'tell me about yourself' in command:
                self.talk('My name is alexa 2 point o developed by jomi,karthika and sera')

            elif 'divide' in command:
                num = command.replace('divide', '')
                num_split = num.split("by")
                divide_ans = self.divideNum(int(num_split[0]), int(num_split[1]))
                self.talk(divide_ans)

            elif 'add' in command:
                num = command.replace('add', '')
                num_split = num.split("and")
                sum_ans = self.addNum(int(num_split[0]), int(num_split[1]))
                self.talk(sum_ans)

            elif 'subtract' in command:
                num = command.replace('subtract', '')
                num_split = num.split("from")
                sub_ans = self.subNum(int(num_split[1]), int(num_split[0]))
                self.talk(sub_ans)

            elif 'multiply' in command:
                num = command.replace('multiply', '')
                num_split = num.split("and")
                mul_ans = self.mulNum(int(num_split[0]), int(num_split[1]))
                self.talk(mul_ans)

            elif 'help' in command:

                self.talk("""start talking by saying alexa
                include the term add or subtract or multiply or divide for arithmetic operations respectively
                if you want to hear a joke include the term joke in your conversation
                if you want to know about anything include the term tell about in your conversation
                if you want to play something from youtube include the term play and the name of the video
                self.talk("if you want to know the current time include the term time in your conversation
                self.talk("you can also know about my personal information like full name,age""")

            elif 'thank you' in command:
                self.talk("good bye")
                return True

            else:
                self.talk("sorry i didn't get you")

        except:
            pass

        return False

    def divideNum(self, num1, num2):
        if(num2 == 0):
            self.talk("divison by 0 error")
        else:
            return num1//num2

    def addNum(self, num1, num2):
        return num1+num2

    def subNum(self, num1, num2):
        return num1-num2

    def mulNum(self, num1, num2):
        return num1*num2


if __name__ == '__main__':
    top.mainloop()
    voice_obj = VoiceBot()
    exitFlag = False
    while exitFlag != True:
        exitFlag = voice_obj.runAlexa()
