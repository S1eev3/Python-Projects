import tkinter as tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        # Button setup and layout for Default html page
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=2, padx=(10,10), pady=(10,10))
        # Button setup and layout for Custom html page
        self.btnSubmit = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btnSubmit.grid(row=2, column=3, padx=(10,10), pady=(10,10))
        # Label setup and layout to display instructions to user
        self.lblCustom = Label(self.master,text='Enter custom text or click the default HTML page button',font=('Helvetica', 12), fg='black')
        self.lblCustom.grid(row=0, column=0, padx=(10,10), pady=(10,10))
        # Entry field setup and layout for user input custom html
        self.txtCustom = Entry(self.master, text='', font=('Helvetica', 12), fg='black', width=65)
        self.txtCustom.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(10,10))


    # Function to create html page with custom user content
    def customHTML(self):
        htmlCustom = self.txtCustom.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlCustom + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
        
        
    # Function to create default html page
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")









if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
