from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp


engine = pp.init()

voices=engine.getProperty('voices')
print(voices)

engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")  #creating instance of class

convo = [
    'Hello',
    'Hi there!',
    'What is your name?',
    'My name is Bot',
    'How are you?',
    'I am doing great these days, thanks for asking',
    'Where are you from?',
    'I am from Ahmedabad',
    'Which language do you prefer to talk?',
    'I mostly talk in english',
    'In which language is your programming done?',
    'I am created using Python.',
    'Who created you?',
    'I am created by Mokshi Shah and Nupur Patel.',
    'What is Python?',
    'Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.'
]

trainer = ListTrainer(bot)         #object

# training the bot with the help of trainer

trainer.train(convo)

main = Tk()  #creating object of Tk class

main.geometry("500x650")

main.title("My Chat bot")

img = PhotoImage(file="bot1.png")

photoL=Label(main,image=img)

photoL.pack(pady=5)


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"you: "+query)
    print(type(answer_from_bot))
    msgs.insert(END,"bot: "+str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)



frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame,width=80,height=16,yscrollcommand=sc.set)

sc.pack(side=RIGHT,fill=Y)

msgs.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

# creating text field

textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X, pady=2)

btn=Button(main,text="Chat with bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()

#creating a function
def enter_function(event):
    btn.invoke()

#going to bind main window with enter key..

main.bind('<Return>', enter_function)

main.mainloop()