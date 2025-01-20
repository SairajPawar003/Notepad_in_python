from tkinter import *
from tkinter.messagebox import showinfo,askquestion,askokcancel
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import os



def new_file():
    global file
    root.title("un_named file Notepad_lite")
    file = None
    text_area.delete(1.0, END) #ffrom line 1st to END line delete all lines

def open_file():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes = [("All Files","*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notpad_lite")
        with open(file,"r") as f:
            text_area.insert(1.0, f.read())
            f.close()
            
def save_file():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Un_named Notepad_lite.txt', defaultextension=".txt" ,filetypes = [("All Files","*.*"), ("Text Documents", "*.txt")])
        
        if file =="":
            file = None
        else:
            with open(file, "w") as f:
                f.write(text_area.get(1.0, END))
                f.close()
                root.title(os.path.basename(file) + "-Notpad_lite")
    else :
        with open(file, "w"):
            f.write(text_area.get(1.0,END))
            f.close()


def exit_app():
    res = askokcancel("Exit","Are you sure want to exit Notepad_lite")
    if res == True:
        root.destroy()
    else:
        # print("succssesfully exited")
        pass


def copy_text():
    text_area.event_generate(("<<Copy>>"))

def cut_text():
    text_area.event_generate(("<<Cut>>"))

def peste_text():
    text_area.event_generate(("<<Paste>>"))

def about_us():
    showinfo("Notepad","Demo clone of notepad made by sairaj pawar")



if __name__=="__main__":

    root=Tk() #starting of code

    
    root.title("Notepad_lite")#title icon and size of our extentin
    root.wm_iconbitmap("pokemon_PNG75.ico")
    root.minsize(800 , 400)
    # root.maxsize(900,700) only up to this size
 ###############################   Adding Text field  #########################################################################
    
    #adding text area in the our project for writing 
    text_area = Text(root, font="Times")    #optional - ("Lucida", 20, "bold")
    file = None #this is a variable for our opening file
    text_area.pack(expand=True, fill=BOTH)  #expand command take size of parent class and fill both can tell about the size can increase in both side
    #text_area.pack()
################################   Adding Menubar  ######################################################################################
  
    #Now creation of our menu bar which contains our file operations and help or about section
    menu_bar = Menu(root)
######################################################################################################################
    #first 
    file_menu = Menu(menu_bar, tearoff=0)   #this tearoff command gives the functionality to extends that command 
    #now our file menu contains some options like new, open, save, etc
    file_menu.add_command(label="New", command= new_file)  #the command denotes the function for that menu
    #open the existing file of your pc
    file_menu.add_command(label="Open", command= open_file)
    #save
    file_menu.add_command(label="Save", command= save_file)
    
    file_menu.add_separator()#this will add an horrizontal line in your menu
    #exit
    file_menu.add_command(label="Exit", command= exit_app)
#######################################################################################################################
    #addinfg this in main menu
    menu_bar.add_cascade(label="File", menu=file_menu)
#######################################################################################################################
    #edit menu
    edit_menu = Menu(menu_bar, tearoff=0) 

    edit_menu.add_command(label="Copy", command= copy_text)
    edit_menu.add_command(label="Cut", command= cut_text)
    edit_menu.add_command(label="Pest", command= peste_text)

    menu_bar.add_cascade(label="Edit", menu=edit_menu)
########################################################################################################################
    help_menu = Menu(menu_bar, tearoff=0) 

    help_menu.add_command(label="About_us", command= about_us)
    
    menu_bar.add_cascade(label="Help", menu=help_menu)
########################################################################################################################

    root.config(menu=menu_bar)#this command helps to you for config all changes and saved it in your device

######################################  Adding Scrollbar in y direction at right side ###################################################################

    scroll_y = Scrollbar(text_area)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=text_area.yview)
    text_area.config(yscrollcommand=scroll_y.set)



    root.mainloop() #note this line is always wrote at the end of our code