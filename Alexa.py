import os
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty("voices")
#for voice in voices:
engine.setProperty('voice',voices[1].id)
pyttsx3.speak("hello my name is alexa")
pyttsx3.speak("what is your name")
name=input()
pyttsx3.speak("how may i help you" + name)
while(True):
    print("please enter your command")
    task=input()

    if (("open" in task) or ("start" in task) or ("execute" in task)) and (("notepad" in task) or ("notes" in task) or ("editor" in task)):
       os.system("notepad")
 
    elif (("open" in task) or ("start" in task) or ("execute" in task)) and (("chrome" in task) or ("browser" in task) or ("explorer" in task)):
       os.system("start chrome")

    elif (("open" in task) or ("start" in task) or ("execute" in task)) and (("terminal" in task) or ("cmd" in task)):
       os.system("start")

    elif (("open" in task) or ("start" in task) or ("execute" in task)) and (("task manager" in task) or ("taskmsg" in task)):
        os.system("taskmgr")

    elif (("open" in task) or ("start" in task) or ("execute" in task)) and (("file explorer" in task) or ("explorer" in task) ):
        os.system("start chrome")

    elif ("stop" in task or "bye" in task or "exit" in task or "no" in task):
        pyttsx3.speak("byeee have a good day ahead")
        exit()

    pyttsx3.speak("what else can i do for you " + name)
