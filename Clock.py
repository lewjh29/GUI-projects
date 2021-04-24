from tkinter import *
import time
from tkinter import messagebox


root = Tk()
root.title("Lewis's Clock")
root.configure(background="black")
root.geometry("400x250")




def clock():
	hour = time.strftime("%I")
	minute = time.strftime("%M")
	second = time.strftime("%S")
	day = time.strftime("%A")
	am_pm = time.strftime("%p")
	date = time.strftime("%x")
	

	my_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm + "\n" + date)
	my_label.after(1000,clock)
	
	my_label2.config(text=day)



def update():
	my_label.config(text="New text")

my_label = Label(root,text="",font=("Helvetica", 48), fg="cyan", bg="black")
my_label.pack(pady=20)

my_label2 = Label(root, text="", font=("Helvetica",26), fg="cyan", bg="black")
my_label2.pack(pady=10)

clock()
root.mainloop()
