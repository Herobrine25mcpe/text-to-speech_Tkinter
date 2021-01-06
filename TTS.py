from tkinter import *
import pyttsx3


window = Tk()
window.title("text-to-speech")
window.geometry('350x450')
window.configure(bg="grey15")

v = IntVar()
v.set("0")

def audio():
    #Voice
    speaker = pyttsx3.init()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate + range.get())
    # Rate
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[v.get()].id)
    speaker.say(textbox.get("1.0", END))
    speaker.runAndWait()

def rbutton(value):
    if value==0:
        label1= Label(window, text = "Voice: Male  ")

    else:
        label1 = Label(window, text="Voice: Female")

#frame
frame = Frame(window, pady= 5, padx = 5).grid(row = 1, column = 0 , sticky = "nsew")

#Enter text label
label1 = Label(window, text = "\u2193ENTER TEXT HERE\u2193", font = ("Arial", 15),bg="grey30")
label1.grid(row = 0, column = 0, sticky=E+W)

# For Entry
scroll = Scrollbar(frame,bg="grey25")
scroll.grid(row = 1 , column = 1, sticky= "ns")
textbox= Text(frame, height = 10, width = 41,bg="grey60", wrap = "word",yscrollcommand = scroll.set)
textbox.grid(row= 1 , column = 0, sticky = "nsew")

label1 = Label(window, text = " SETTINGS", font = ("Arial", 15),bg="grey25")
label1.grid(pady = 10,padx =10,row = 3, column = 0, sticky=E+W)

label1 = Label(window, text = " Voice ", font = ("Arial", 15),bg="grey25")
label1.grid(pady = 10,row = 4, column = 0, sticky=W)

Radiobutton(window, text = "Male",bg="grey15", variable = v, value = 0, command=lambda: rbutton(v.get())).grid(row = 5, sticky= W)
Radiobutton(window, text = "Female",bg="grey15", variable = v, value = 1,command=lambda: rbutton(v.get())).grid(row = 6, sticky = W)

label1 = Label(window, text = "   Rate   ", font = ("Arial", 15),bg="grey25")
label1.grid(pady = 10,row = 4, column = 0)

range= Scale(window, from_ = -200 ,to =200, length=200,bg="grey25", orient = HORIZONTAL)
range.grid(row= 5 , column = 0, sticky=E)


button1 = Button(window,bg="grey20", text = "Convert",command = audio)
button1.grid(pady = 10,row = 2)

#Ver
label1 = Label(window, text = "Ver:0.1.0", font = ("Arial", 8),background ="grey25")
label1.grid(pady = 10,row = 10, column = 0, sticky=E+W)


scroll.config(command = textbox.yview,bg="grey25")

window.mainloop()
