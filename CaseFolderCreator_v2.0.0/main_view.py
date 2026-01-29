import tkinter as tk


class MainView:

    def __init__(self, root, controller):

        #Root Window
        self.root_window = root
        self.controller = controller

        self._build_ui()
    
    def _build_ui(self) -> None:
        self.root_window.title("Case File Generator")
        self.root_window.geometry('950x500')

        self.caseNumberLabel = tk.Label(self.root_window, text = "Case Number")
        self.caseNumberLabel.grid(column=0, row=0, padx=10)
        self.caseNumberEntry = tk.Entry(self.root_window, width = 20)
        self.caseNumberEntry.grid(column=0, row=1, padx= 10)

        self.agentLabel = tk.Label(self.root_window, text = "Case Agent (LAST NAME ONLY)")
        self.agentLabel.grid(column=1, row=0, padx = 10)
        self.agentEntry = tk.Entry(self.root_window, width = 20)
        self.agentEntry.grid(column=1, row=1, padx= 10)

        itemNumLabel = tk.Label(self.root_window, text = "Number of Line items (INTEGER ONLY)")
        itemNumLabel.grid(column=2, row=0, padx= 10)
        self.itemNumEntry = tk.Entry(self.root_window, width = 5)
        self.itemNumEntry.grid(column=2, row=1, padx = 10)

        directorySelectorLabel = tk.Label(self.root_window, text = "Select Case Folder Location")
        directorySelectorLabel.grid(column=0, row=2, pady=10)
        self.directorySelectorEntry = tk.Entry(self.root_window, width=50)
        self.directorySelectorEntry.grid(column=0, row= 3, padx=10)

        enterButton = tk.Button(self.root_window, text= "Continue", command= self.controller.continue_button_clicked)
        enterButton.grid(column=3, row= 0, pady = 10)

        directorySelectorButton = tk.Button(self.root_window, text="Browse...", command=self.controller.directory_button_clicked)
        directorySelectorButton.grid(column=1, row=3)

        #profileButton = tk.Button(self.root_window, text = "Edit Profile", command= self.profileCreatorWindow)
        #profileButton.grid(column=3, row = 4)

        self.isCybertipCheckbox = tk.Checkbutton(self.root_window, text = "Cybertip", command=self.controller.cyberTip_box_checked)
        self.isCybertipCheckbox.grid(column = 2, row = 3)

        self.attachmentsLabel = tk.Label(self.root_window, text="Attachments")
        self.attachmentsLabel.grid(column=0, row=4, pady=10)

        self.attachmentsListBox = tk.Listbox(self.root_window, width=75)
        self.attachmentsListBox.grid(column=0, row=5)

        self.attachmentsAddButton = tk.Button(self.root_window, text="Add", command=self.controller.add_attchment_button)
        self.attachmentsAddButton.grid(column=0, row=6)

        self.attachmentsRemoveButton = tk.Button(self.root_window, text="Remove", command=self.controller.remove_attachment_button)
        self.attachmentsRemoveButton.grid(column=0, row=7)

    def run(self) -> None:
        self.root_window.mainloop()
    
    def set_directory_entry(self, path: str) -> None:
        self.directorySelectorEntry.delete(0, tk.END)
        self.directorySelectorEntry.insert(0, path)
    
    def add_attachment(self, attc: str) -> None:
        self.attachmentsListBox.insert(tk.END, attc)
    def remove_attchment(self, attc_index: int) -> None:

        try:
            self.attachmentsListBox.delete(attc_index, attc_index)
        except tk.TclError:
            print("Non-fatal error: Unable to remove attachment, likely none selected")
    
class ProfileView:
    pass

class ItemView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.window = tk.Toplevel(parent)
        self.entries = []

        itemCount = controller.get_item_count()

        self.window.title("Line Items")
        
        itemWindowLabel = tk.Label(self.window, text="Enter Line Items Below:")
        itemWindowLabel.grid(row=0, column=0, pady=10)

        for i in range(itemCount):
            entry = tk.Entry(self.window, width = 10)
            entry.grid(row=i, column=0, padx=5, pady=5)
            self.entries.append(entry)
        
        saveButton = tk.Button(self.window, text='Save', command = self.controller.items_saved)
        saveButton.grid(pady=10)





