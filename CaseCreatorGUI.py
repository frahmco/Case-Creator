from tkinter import * 
from CaseFileCreator import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import END

class CaseGUI:

    #Class declarations for things MOVE TO __init__
    itemList = []
    itemEntries = []
    caseNumber = ''
    agent = ''
    itemNum = 0
    root_window = Tk()
    caseNumber = ''
    directory = ''
    isCyberTip = BooleanVar()

    #Change this to change default CT path
    TIP_DEFAULT_PATH = "X:\\__New Cybertip triage\\"

    

    #Start window when object is built
    def __init__(self):
        self.initializeWindow()


    def initializeWindow(self):

        #Global declarations for entry boxes
        global caseNumberEntry
        global agentEntry
        global itemNumEntry
        global directorySelectorEntry
        global caseNumberLabel
        global agentLabel

        #GUI set-up
        
        self.root_window.title("Case File Generator")
        self.root_window.geometry('900x150')

        caseNumberLabel = Label(self.root_window, text = "Case Number")
        caseNumberLabel.grid(column=0, row=0, padx=10)
        caseNumberEntry = Entry(self.root_window, width = 20)
        caseNumberEntry.grid(column=0, row=1, padx= 10)

        agentLabel = Label(self.root_window, text = "Case Agent (LAST NAME ONLY)")
        agentLabel.grid(column=1, row=0, padx = 10)
        agentEntry = Entry(self.root_window, width = 20)
        agentEntry.grid(column=1, row=1, padx= 10)

        itemNumLabel = Label(self.root_window, text = "Number of Line items (INTEGER ONLY)")
        itemNumLabel.grid(column=2, row=0, padx= 10)
        itemNumEntry = Entry(self.root_window, width = 5)
        itemNumEntry.grid(column=2, row=1, padx = 10)

        directorySelectorLabel = Label(self.root_window, text = "Select Case Folder Location")
        directorySelectorLabel.grid(column=0, row=2, pady=10)
        directorySelectorEntry = Entry(self.root_window, width=50)
        directorySelectorEntry.grid(column=0, row= 3, padx=10)

        enterButton = Button(self.root_window, text= "Continue", command=self.continueButtonClicked)
        enterButton.grid(column=3, row= 0, pady = 10)

        directorySelectorButton = Button(self.root_window, text="Browse...", command=self.directoryBrowse)
        directorySelectorButton.grid(column=1, row=3)

        isCybertipCheckbox = Checkbutton(self.root_window, text = "Cybertip", command= self.isCyberTipBoxChecked, variable= self.isCyberTip)
        isCybertipCheckbox.grid(column = 2, row = 3)

        self.root_window.mainloop()


    def finishButtonHandler(self): #Probably can delete this
        self.finishButtonClickedAction()

    def finishButtonClickedAction(self):
        caseNumber = caseNumberEntry.get()
        agent = agentEntry.get()
        itemNum = int(itemNumEntry.get())
        
        for i in range (0, itemNum):
            self.itemList.append(self.itemEntries[i].get())

        fileCreator = CaseFileCreator()
        fileCreator.createDirectories(caseNumber, agent, self.itemList, self.directory)
        self.root_window.destroy()

    def continueButtonClicked(self):
        itemNum = itemNumEntry.get()

        if (self.isCyberTip.get()):
            fileCreator = CaseFileCreator()
            fileCreator.createCybertipDirectories(caseNumberEntry.get(), agentEntry.get(), directorySelectorEntry.get())
            self.root_window.destroy()

        elif (itemNum.isnumeric() == False):
            messagebox.showerror("ERROR", "Error: Number of line items MUST be an integer!")
        #if (caseNumberEntry.get() == ''):
            #if(messagebox.askretrycancel("WARNING", "Warning: Case number field is empty.") == False):
                #self.root_window.destroy()
            #else:
                #pass

        else:
            itemNum = int(itemNum)
            itemEntryWindow = Toplevel()
            itemEntryWindow.title("Line Items")

            itemEntryLabel = Label(itemEntryWindow, text="Enter Line Items")
            itemEntryLabel.grid(column=0, row=0, padx=5, pady= 5)

            for i in range (0, itemNum):
                self.itemEntries.append(Entry(itemEntryWindow, width=10))
                self.itemEntries[i].grid(column= 0, row = i + 1, padx=5, pady=5)

            finishButton = Button(itemEntryWindow, text= "Finish", command=self.finishButtonHandler)
            finishButton.grid(padx=5,pady=5)

    def directoryBrowse(self):
        self.directory = filedialog.askdirectory()
        directorySelectorEntry.delete(0, END)
        directorySelectorEntry.insert(0, self.directory)

    def isCyberTipBoxChecked(self):

        if (self.isCyberTip.get()):
            itemNumEntry.delete(0, END)
            itemNumEntry.configure(state="disabled", disabledbackground= "gray")

            directorySelectorEntry.insert(0, self.TIP_DEFAULT_PATH)

            caseNumberLabel.config(text = "CyberTip Number")

            agentLabel.config(text = "Electronic Service Provider")

        else:
            agentEntry.configure(state="normal")
            itemNumEntry.configure(state="normal")

            caseNumberLabel.config(text = "Case Number")
            agentLabel.config(text = "Case Agent (LAST NAME ONLY)")

            directorySelectorEntry.delete(0, END)
            