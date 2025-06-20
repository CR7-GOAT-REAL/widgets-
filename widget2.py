#import neccary libraries
from tkinter import *
from datetime import date

#create window
window = Tk()

#set the window title and geometry
window.title('Demo Window')
window.geometry('400x300')

lb1 = Label(text= "Hello", fg= "White", bg= "Blue", height = 1, width = 300)
name_lb1 = Label(text= "Fullname", bg= "Yellow")
name_entry = Entry()
def display():
    name = name_entry.get()

    global message
    message = "Welcome To The Application! the date is:"
    greet = "Hello" +name+ "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)
btn = Button(text="Begin", command=display, height=1, bg="green", fg ="White")
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()