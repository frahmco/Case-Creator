from tkinter import * 
from CaseFileCreator import *
from profile_templates import *
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

    profileName = ''
    profileAgency = ''
    profileBadgeNumber = ''
    profileTitle = ''
    profileDefaultPath = ''

    #Change this to change default CT path
    TIP_DEFAULT_PATH = "X:\\__New Cybertip triage\\"

    

    #Start window when object is built
    def __init__(self):
        self.initializeWindow()


    def initializeWindow(self):

        #Global declarations for entry boxes FIX THIS IS HORRIBLE
        global caseNumberEntry
        global agentEntry
        global itemNumEntry
        global directorySelectorEntry
        global caseNumberLabel
        global agentLabel
        global examinerInfoLabel

        #GUI set-up
        
        self.root_window.title("Case File Generator")
        self.root_window.geometry('950x250')

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

        profileButton = Button(self.root_window, text = "Edit Profile", command= self.profileCreatorWindow)
        profileButton.grid(column=3, row = 4)

        isCybertipCheckbox = Checkbutton(self.root_window, text = "Cybertip", command= self.isCyberTipBoxChecked, variable= self.isCyberTip)
        isCybertipCheckbox.grid(column = 2, row = 3)

        if not Profile.profileCheck():
            self.profileCreatorWindow()

        else:
            profile = Profile()
            loaded_profile = profile.readProfile()

            directorySelectorEntry.insert(0, loaded_profile.getDefaultPath())
            self.profileName = loaded_profile.getFirstName() + ' ' + profile.getLastName()
            self.profileAgency = loaded_profile.getAgency()
            self.profileBadgeNumber = loaded_profile.getBadgeNumber()
            self.profileTitle = loaded_profile.getTitle()
            self.profileDefaultPath = loaded_profile.getDefaultPath()

        textBoxInfo = "User Info:\n\n" + self.profileTitle + ' ' + self.profileName + ' #' + self.profileBadgeNumber + '\n' + self.profileAgency + '\n' + self.profileDefaultPath
        examinerInfoLabel = Label(self.root_window, text= textBoxInfo, borderwidth=1, relief=SOLID, pady=5)
        examinerInfoLabel.grid(column= 3, row = 3)

        self.root_window.mainloop()
    def updateInfoLabel(self):
        newText = "User Info:\n\n" + self.profileTitle + ' ' + self.profileName + ' #' + self.profileBadgeNumber + '\n' + self.profileAgency + '\n' + self.profileDefaultPath
        examinerInfoLabel.config(text= newText)
        

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
        selectedDir = filedialog.askdirectory()
        self.directory = selectedDir #THIS IS BAD PRACTICE FIX ME!!!
        directorySelectorEntry.delete(0, END)
        directorySelectorEntry.insert(0, self.directory)

        if Toplevel.winfo_exists(profileEditWindow):
            defaultPathEntryBox.delete(0, END)
            defaultPathEntryBox.insert(0, self.directory)
        else:
            pass

        return selectedDir

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

    def generateProfile(self):
        fN = firstNameEntryBox.get()
        lN = lastNameEntryBox.get()
        a = agencyEntryBox.get()
        bN = badgeNumberEntryBox.get()
        t = titleEntryBox.get()
        dP = defaultPathEntryBox.get()

        profile = Profile(fN, lN, a, bN, t, dP)
        profile.createProfile()



    def profileCreatorWindow(self): #Window for Profile creation...also includes profile generation.
        global profileEditWindow

        profileEditWindow = (Toplevel())
        profileEditWindow.attributes("-topmost", True)
        profileEditWindow.title("Profile Editor")

        global firstNameEntryBox
        global lastNameEntryBox
        global agencyEntryBox
        global badgeNumberEntryBox
        global titleEntryBox
        global defaultPathEntryBox

        firstNameLabel = Label(profileEditWindow, text="First Name")
        firstNameLabel.grid(column= 0, row= 0)
        firstNameEntryBox = Entry(profileEditWindow, width= 20)
        firstNameEntryBox.grid(column = 0, row= 1, padx = 2.5)

        lastNameLabel = Label(profileEditWindow, text = "Last Name")
        lastNameLabel.grid(column=1, row = 0)
        lastNameEntryBox = Entry(profileEditWindow, width= 20)
        lastNameEntryBox.grid(column=1, row= 1, padx = 2.5)

        agencyLabel = Label(profileEditWindow, text = "Agency")
        agencyLabel.grid(column = 0, row = 2)
        agencyEntryBox = Entry(profileEditWindow, width= 10)
        agencyEntryBox.grid(column=0, row=3)

        badgeNumberLabel = Label(profileEditWindow, text = "Badge Number")
        badgeNumberLabel.grid(column=0, row=4)
        badgeNumberEntryBox = Entry(profileEditWindow, width= 10)
        badgeNumberEntryBox.grid()

        titleLabel = Label(profileEditWindow, text="Title")
        titleLabel.grid()
        titleEntryBox = Entry(profileEditWindow, width= 10)
        titleEntryBox.grid()

        defaultPathLabel = Label(profileEditWindow, text="Default Save Path")
        defaultPathLabel.grid()
        defaultPathEntryBox = Entry(profileEditWindow, width= 50)
        defaultPathEntryBox.grid()

        def generateProfile():
            fN = firstNameEntryBox.get()
            lN = lastNameEntryBox.get()
            a = agencyEntryBox.get()
            bN = badgeNumberEntryBox.get()
            t = titleEntryBox.get()
            dP = defaultPathEntryBox.get()

            profile = Profile(fN, lN, a, bN, t, dP)
            profile.createProfile()

            self.profileName = profile.getFirstName() + ' ' + profile.getLastName()
            self.profileAgency = profile.getAgency()
            self.profileBadgeNumber = profile.getBadgeNumber()
            self.profileTitle = profile.getTitle()
            self.profileDefaultPath = profile.getDefaultPath()

            self.updateInfoLabel()

            profileEditWindow.destroy()

        saveButton = Button(profileEditWindow, text= "Save", command= generateProfile)
        saveButton.grid()

        browseButton = Button(profileEditWindow, text="Browse...", command= self.directoryBrowse)
        browseButton.grid(column= 1, row = 9)


            