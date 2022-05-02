import pyttsx3
import PyPDF2
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import threading

window = Tk()
window.title("AudiobookAI")
window.geometry('390x540')

v = IntVar()
v.set("0")


def cls1():
    textbox.delete(1.0, END)

def cls2():
    textboxp.delete(1.0, END)

def audio_():
    speaker = pyttsx3.init()
    # Voice
    speaker = pyttsx3.init()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate + range1.get())
    # Rate
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[v.get()].id)
    speaker.say(textboxp.get("1.0",END))
    speaker.runAndWait()

def thread():
    x = threading.Thread(target=audio_)
    x.start()

def pdf_():
    filelocation = askopenfilename()
    book = open(filelocation, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book,strict=False)
    pages= pdfReader.numPages
    plabel = Label(tab2, text="total pages:" + str(pages))
    plabel.grid(row=3)
    p1 = int(e1.get())
    p2 = int(e2.get())
    for x in range(p2-1,p1-2,-1):
        page = pdfReader.getPage(x)
        text = page.extractText()
        textboxp.insert(1.0,text)
        plabel = Label(window, text="page num: "+ str(x))
        plabel.grid(row=2)

def tpages():
    filelocation = askopenfilename()
    book = open(filelocation, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book,strict=False)
    pages= pdfReader.numPages
    plabel = Label(tab2, text="total pages:" + str(pages))
    plabel.grid(row=3)

def text_():
    speaker = pyttsx3.init()
    #Voice
    speaker = pyttsx3.init()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate + range1.get())
    # Rate
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[v.get()].id)
    speaker.say(textbox.get("1.0",END))
    speaker.runAndWait()

def rbutton(value):
    if value==0:
        label1= Label(tab3, text = "Voice: Male  ")
        label1.grid(row =12)
    else:
        label1 = Label(tab3, text="Voice: Female")
        label1.grid(row=12)

def scale(s):
    label = Label(tab3, text="Rate: " + str(range1.get()))
    label.grid(row=10, column=0)


tab_control = ttk.Notebook(window)

tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)

tab_control.add(tab1, text='Text')
tab_control.add(tab2, text='PDF')
tab_control.add(tab3, text='Settings')

#tab1

label1 = Label(tab1, text = "\u2193Enter text here \u2193", font = ("Arial", 15),background = 'white')
label1.grid(row = 0, column = 0, sticky=E+W)


scroll = Scrollbar(tab1)
scroll.grid(row = 1 , column = 1, sticky= "ns")
textbox= Text(tab1, height = 20, width = 41, wrap = "word",yscrollcommand = scroll.set)
textbox.grid(row= 1 , column = 0, sticky = "nsew")

button1 = Button(tab1, text = "Convert",command = text_)
button1.grid(pady = 20,row = 2)
button1 = Button(tab1, text = "Clear",command = cls1)
button1.grid(pady = 10,padx=10,row = 3, column = 0, sticky = W)
button1 = Button(tab1, text = "Close",command = window.quit)
button1.grid(pady = 10,padx=10,row = 3, column = 0, sticky=E)


#tab2

label1 = Label(tab2, text = "Select a pdf file", font = ("Arial", 15),background = 'white')
label1.grid(row = 0, column = 0, sticky=E+W)

scroll = Scrollbar(tab2)
scroll.grid(row = 1 , column = 1, sticky= "ns")
textboxp= Text(tab2, height = 15, width = 41, wrap = "word",yscrollcommand = scroll.set)
textboxp.grid(row= 1 , column = 0, sticky = "nsew")

plabel1 = Label(tab2, text="First page")
plabel1.grid(row=2,column=0, pady=5,padx=10,sticky= W)
plabel2 = Label(tab2, text="page num:0")
plabel2.grid(row=2)
plabel3 = Label(tab2, text="Last page")
plabel3.grid(row=2,padx=10,column=0,sticky= E)
e1=Entry(tab2, width = 10)
e1.grid(row=3,column=0, pady=5,padx=10,sticky= W)
e2=Entry(tab2, width = 10)
e2.grid(row=3,padx=10,column=0,sticky= E)


button1 = Button(tab2, text = "Open",command = pdf_)
button1.grid(pady = 10,row = 4)


button1 = Button(tab2, text = "Convert",command =thread)
button1.grid(pady = 10,row = 5)

button1 = Button(tab2, text = "Clear",command = cls2)
button1.grid(pady = 10,padx=10,row = 6, column = 0, sticky = W)

button1 = Button(tab2, text = "Close",command = window.quit)
button1.grid(pady = 10,padx=10,row = 6, column = 0, sticky=E)

button1 = Button(tab2, text = "Check No.of Pages",command = tpages)
button1.grid(pady = 10,padx=10,row = 6, column = 0)

scroll.config(command = textboxp.yview)


#tab3
label1 = Label(tab3, text = "Select the setting you want to apply", font = ("Arial", 15),background = 'white', foreground = "black")
label1.grid(row = 0, column = 0, sticky=E+W)

label1 = Label(tab3, text = "Rate", font = ("Arial", 15),background = 'white')
label1.grid(pady = 10,row = 1, column = 0, sticky=E+W)
range1= Scale(tab3, from_ = -200 ,to =200, orient = HORIZONTAL, command= scale,length= 300)
range1.grid(row= 2 , column = 0, sticky = W, padx =10)

label1 = Label(tab3, text = "Voice", font = ("Arial", 15),background = 'white')
label1.grid(pady = 10,row = 3, column = 0, sticky=E+W)
rbutton1 = Radiobutton(tab3, text = "Male", variable = v, value = 0, command=lambda: rbutton(v.get()))
rbutton1.grid(row = 4, sticky= W)
rbutton2 = Radiobutton(tab3, text = "Female", variable = v, value = 1,command=lambda: rbutton(v.get()))
rbutton2.grid(row = 5, sticky = W)

rlabel = Label(tab3, text="Rate: 0")
rlabel.grid(row=10, column=0)
vlabel= Label(tab3, text = "Voice: Male")
vlabel.grid(row =12)

#Ver
label1 = Label(tab3, text = "Ver:0.1.0", font = ("Arial", 8),background = 'white')
label1.grid(pady = 190,row = 20, column = 0, sticky=E+W)

tab_control.grid(row = 0, column = 0)

window.mainloop()
