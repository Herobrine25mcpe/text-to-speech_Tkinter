# text-to-speech_Tkinter
 this is project is a simple text to speech converter which uses Tkinter for the GUI and can also read a pdf.  



#Requirements
So in order to make it work you need to install a few things to get the whole thing working. the project is entierly written in python.

you need to install pyttsx3, which is the python library for text to speech.

      >pip install pyttsx3
      >pip install PyPdf2     

and install PyPDF2, which is the python library for messing around with the pdf files.

after you pip install both of these library. the code should work without any problem.

# Text box
 Enter text in the texbox, then hit enter and you should hear a robotic speech.
 
![](images/text.png)

# Pdf box
 Select a pdf file and then check the number of pages. 
 Then you can select starting page and end page of the pdf and then open the pdf. The text from defiened pages will get inserted into the textbox, from hear     just hit convert and you can hear the text no problem.

![](images/pdf.png)

# Settings box
You can select male or female voice here and also the rate at which the speaker talks. 
the rate goes from -100(slowest) to 100(fastest)

![](images/settings.png)


