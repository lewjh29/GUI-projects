import tkinter as tk

class Timer:
    def __init__(self, master):
        self.master = master
        master.title("Revision - 16 Hour Timer")

        self.state = False
        self.hours = 16
        self.minutes = 0
        self.seconds = 0

        self.hrs = 16
        self.mins = 0
        self.secs = 0


        self.display = tk.Label(master,width=10,height=3,bg="black")
        self.display.config(text="16:00:00", font=("Helvetica bold",42),fg="cyan")
        self.display.grid(row=0, column=0, columnspan=2, rowspan=3)


        self.start_button = tk.Button(master,fg="cyan", bg="black", activebackground="black", text="Start", width=8, height=6, command=self.start)
        self.start_button.grid(row=0, column=3)

        self.pause_button = tk.Button(master,fg="cyan", bg="black", activebackground="black", text="Pause", width=8,height=3, command=self.pause)
        self.pause_button.grid(row=1, column=3)


        self.resume_button = tk.Button(master,fg="cyan", bg="black", activebackground="black", text="Resume", width=8, height=3, command=self.resume)
        self.resume_button.grid(row=2, column=3)


    def countdown(self):
        

        if self.state == True:

            if (self.hrs == 0) and (self.mins == 0) and (self.secs == 0):
                self.display.config(text="Done!")
                self.state = False
            else:
                self.display.config(text="%02d:%02d:%02d" % (self.hrs,self.mins, self.secs))

                if self.mins == 0:
                	self.hrs -=1
                	self.mins = 59
                	self.secs = 59
                
                elif self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                

                else:
                    self.secs -= 1

                self.master.after(1000, self.countdown)

    def start(self):
        if self.state == False:
            self.state = True
            self.hrs = self.hours
            self.mins = self.minutes
            self.secs = self.seconds
            self.countdown()

    def pause(self):
        if self.state == True:
            self.state = False

    def resume(self):
    	if self.state == False:
    		self.state = True
    		self.countdown()


root = tk.Tk()
my_timer = Timer(root)

root.mainloop()
"{:02} : {:02}".format(10, 0)


	
