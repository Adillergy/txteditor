from tkinter import Tk , scrolledtext , filedialog , Menu , END , messagebox


root = Tk(className=" Text Editor")
textArea = scrolledtext.ScrolledText(root , width = 100 , height = 80)

#functions

def newFile():
    if len(textArea.get('1.0' , END+'-1c'))>0:
        if messagebox.askyesno("Save" , "Do you wish to save?"):
            saveFile()
        else:
            textArea.delete('1.0' , END)
def openFile():
    file = filedialog.askopenfile(parent = root  , mode = 'rb' , title = 'Select a File' , filetypes= ((" Text File " , "*.txt") , (" All Files " , "*.*")))

    if file!=None:
        contents = file.read()
        textArea.insert('1.0' , contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode = 'w')
    if file!=None:
        data=textArea.get('1.0' , END+'-1c')
        file.write(data)
        file.close()

def exit():
    if len(textArea.get('1.0' , END+'-1c'))>0:
        if messagebox.askyesno("Save" , "Do you wish to save and quit?"):
            saveFile()
            root.destroy()
        else:
            root.destroy()   

def about():
    label = messagebox.showinfo("About" , "Lame text editor lol.") 

def faq():
    label = messagebox.showinfo("FAQ" , "Srsly? , Pls get a life.") 






#menu
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label = "File" , menu =fileMenu)
fileMenu.add_command(label="New" , command = newFile)
fileMenu.add_command(label="Open" , command = openFile)
fileMenu.add_command(label="Save" , command =  saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit" , command = exit)



helpMenu=Menu(menu)
menu.add_cascade(label = "Help" , menu =helpMenu)
helpMenu.add_command(label = "FAQ" , command = faq)
helpMenu.add_command(label = "About" , command = about)




textArea.pack()
root.mainloop()