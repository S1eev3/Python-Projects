
import tkinter
from tkinter import *


# Define class for master window
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        # Master window dimensions and attributes
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

        # Initializing variables
        self.varFName = StringVar()
        self.varLName = StringVar()

        # Defining layout of labels for Fname Lname and output display
        self.lblFName = Label(self.master,text='First Name: ', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLName = Label(self.master,text='Last Name: ', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(10,0), pady=(30,0))
        
        # Defining layout of entry fields
        self.txtFName = Entry(self.master,text=self.varFName, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1, padx=(10,0), pady=(30,0))

        self.txtLName = Entry(self.master,text=self.varLName, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(10,0), pady=(30,0))

        # Defining layout of submit and cancel buttons
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    # Submit function to display user entry
    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
        

    # Cancel function to close app
    def cancel(self):
        self.master.destroy()
        





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
