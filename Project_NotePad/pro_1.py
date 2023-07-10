from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(filetypes=[("All Files", "*.*")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    global selected
    if cut.selection_get():
        selected = cut.selection_get()
        cut.delete("sel.first","sel.last")

def copy():
    TextArea.event_generate(("<>"))

def paste():
    TextArea.event_generate(("<>"))

def view():
    showinfo("Notepad","Welcome to my small Project")

if __name__ == '__main__':
    
    root = Tk()
    root.title("Dev's - Notepad")
    root.wm_iconbitmap("Project_NotePad/icons/note.ico")
    root.geometry("644x788")

    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    
    MenuBar = Menu(root)

    FileMenu = Menu(MenuBar, tearoff=0)
   
    FileMenu.add_command(label="New", command=newFile)

    FileMenu.add_command(label="Open", command = openFile)

    FileMenu.add_command(label = "Save", command = saveFile)
    
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    
    EditMenu = Menu(MenuBar, tearoff=0)
    
    EditMenu.add_command(label = "Cut", command=lambda:cut(1))
    EditMenu.add_command(label = "Copy", command=lambda:copy(1))
    EditMenu.add_command(label = "Paste", command=lambda:paste(1))

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=view)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    root.mainloop()