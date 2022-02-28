from tkinter import *
import googletrans
from googletrans import Translator
import win32com.client as tts
import speech_recognition as stt
from gtts import gTTS
from playsound import playsound
import os

master = Tk()
master.geometry('605x400')
master.title('AKMR Translator')
master.resizable(False,False)
master['background']='#3a3b3c'

def transl():
    def transll():
        lname=clickedl.get()
        for i in range(0,va,1):
             if lname==list_values[i]:
                 lnameindex=list_values.index(lname)
                 lcode=list_keys[lnameindex]
                 return lcode
        
    def translc():
        lname=clickedc.get()
        for i in range(0,va,1):
             if lname==list_values[i]:
                 lnameindex=list_values.index(lname)
                 lcode=list_keys[lnameindex]
                 return lcode
    lcode1=transll()
    lcode2=translc()
    etxt=entry1.get()
    translator = Translator()
    trans = translator.translate(etxt, src=lcode1, dest=lcode2)
    entry2.insert(0, trans.text)

def tts_get():

    def reset():
        entry_field.delete(0,END)

    def tts():
        Message = entry_field.get()
        speech = gTTS(text = Message)
        speech.save('tts.mp3')
        playsound('tts.mp3')
        os.remove('tts.mp3')
    
    master1=Tk()
    master1.geometry('605x400')
    master1.title('AKMR Text-To-Speech')
    master1.resizable(False,False)
    master1['background']='#3a3b3c'

    label1 =Label(master1,text='Enter words',font=('times',15,'italic bold'),bg='#E4E6EB', fg='BLACK')
    label1.grid(row=0, column=0, pady=2, ipadx=13, ipady=5, padx=2)

    Msg = StringVar()
    entry_field = Entry(master1, width=30, textvariable = Msg ,font=('times',15,'italic bold'))
    entry_field.grid(row=1, column=1, columnspan=2, ipadx=70, ipady=15, padx=2, pady=2)
   
    btn6 = Button(master1,text='Listen',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'), command=tts)
    btn6.grid(row=2, column= 0, ipady=5, ipadx=34, pady=2)

    btn7 = Button(master1,text='Reset',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'), command=reset)
    btn7.grid(row=2, column= 1, ipady=5, ipadx=30, padx=2, pady=2)

    btn8 = Button(master1,text='Exit',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'), command=master1.quit)
    btn8.grid(row=2, column= 2, ipady=5, ipadx=30, pady=2)

def stt_get():
    def reset():
        entry_box.delete(0,END)

    def sttt():
        reset()

        obj=stt.Recognizer()
        with stt.Microphone() as source:
            audio=obj.listen(source)
            teext=obj.recognize_google(audio)
            print(teext)
            entry_box.insert(0,teext)
    def sttt_lis():
        speaker = tts.Dispatch("SAPI.SpVoice")
        lis_text=entry_box.get()
        speaker.Speak(lis_text)
    
    master2=Tk()
    master2.geometry('605x400')
    master2.title('AKMR Speech-To-Text')
    master2.resizable(False,False)
    master2['background']='#3a3b3c'

    btn9 = Button(master2,text='Tap To Speak',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'), command=sttt)
    btn9.grid(row=0, column= 0, ipady=5, ipadx=30, pady=2)

    entry_box = Entry(master2, width=30, font=('times',15,'italic bold'))
    entry_box.grid(row=1, column=1, columnspan=2, ipadx=70, ipady=15, padx=2, pady=2)
   
    btn10 = Button(master2,text='Listen',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'), command=sttt_lis)
    btn10.grid(row=2, column= 0, ipady=5, ipadx=34, pady=2)

    btn7 = Button(master2,text='Reset',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'), command=reset)
    btn7.grid(row=2, column= 1, ipady=5, ipadx=30, padx=2, pady=2)

    btn8 = Button(master2,text='Exit',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'), command=master2.quit)
    btn8.grid(row=2, column= 2, ipady=5, ipadx=30, pady=2)


############################################################
label1 =Label(master,text='Enter words',font=('times',15,'italic bold'),bg='#E4E6EB', fg='BLACK')
label1.grid(row=0, column=0, pady=2, ipadx=13, ipady=5, padx=2)

varname1 = StringVar()
entry1 = Entry(master, width=30, textvariable=varname1, font=('times',15,'italic bold'))
entry1.grid(row=1, column=1, columnspan=2, ipadx=70, ipady=15, padx=2, pady=2)

list_values=[]
for k in googletrans.LANGUAGES.values():
    list_values.append(k)
va=len(list_values)

options_s= list_values
clickedl = StringVar(master, list_values)
clickedl.set( "Select Language" )
drop_s= OptionMenu(master, clickedl, *options_s)
drop_s.config(bg="#8899A6", fg="WHITE")
drop_s.grid(row=1, column= 0, ipady=8, ipadx=1, padx=2, pady=2)
############################################################

############################################################
list_keys=[]
for k in googletrans.LANGUAGES.keys():
    list_keys.append(k)
ka=len(list_keys)

options_d= list_values
clickedc = StringVar()
clickedc.set( "Select Language" )
drop_d= OptionMenu(master, clickedc, *options_d)
drop_d.config(bg="#8899A6", fg="WHITE")
drop_d.grid(row=2, column= 0, padx=8, ipady=10, ipadx=1, pady=2)

btn1 = Button(master,text='Translate',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'),command=transl)
btn1.grid(row=2, column= 1, ipady=5, ipadx=30, padx=3, pady=2)

btn2 = Button(master,text='Exit',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'), command=master.quit)
btn2.grid(row=2, column= 2, ipady=5, ipadx=50, padx=3, pady=2)
############################################################

############################################################  LABELS
label2 =Label(master,text='Translated',font=('times',15,'italic bold'),bg='#E4E6EB', fg='BLACK')
label2.grid(row=3, column=0, pady=3, ipadx=19, ipady=15, padx=2)

varname2 = StringVar()
entry2 =Entry(master,width=30,textvariable=varname2,font=('times',15,'italic bold'))
entry2.grid(row=3, column=1, columnspan=2, ipadx=70, ipady=15, padx=2)
############################################################

############################################################
btn4 = Button(master,text='Text-To-Speech',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'), command=tts_get)
btn4.grid(row=4, column= 1, ipady=5, ipadx=30, padx=2, pady=2)

btn5 = Button(master,text='Speech-To-Text',bg='#8899A6', fg="WHITE", activebackground='white',font=('times',15,'italic bold'), command=stt_get)
btn5.grid(row=4, column= 2, ipady=5, ipadx=30, pady=2)
############################################################

master.mainloop()