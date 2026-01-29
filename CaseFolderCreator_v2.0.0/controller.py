import tkinter as tk
from tkinter import messagebox, filedialog

from main_view import MainView, ItemView
from model import MainModel
from file_creator import FileCreator
from log import Logger

#Controller for entire program

class MainController:

    def __init__(self):
        self.logfile = Logger()
        self.mainModel = MainModel(self.logfile)
        self.root_window = tk.Tk()
        self.mainView = MainView(self.root_window, self)

        self.fileCreator = (FileCreator(self.logfile))

    def run(self) -> None:
        self.mainView.run()

    #Retrieves and updates model with data input in GUI
    def continue_button_clicked(self) -> None:
        caseNumber = self.mainView.caseNumberEntry.get().strip()
        caseAgent = self.mainView.agentEntry.get().strip()
        lineItems = self.mainView.itemNumEntry.get()
        directory = self.mainView.directorySelectorEntry.get().strip()

        try:
            self.mainModel.update_case_info(caseNumber, caseAgent, lineItems, directory)
        except ValueError as e:
            messagebox.showerror(title="Error", message=f"{e}")

        self.itemView = ItemView(self.root_window, self)
    #Asks for directory selection and updates model and view
    def directory_button_clicked(self) -> None:
        directory = filedialog.askdirectory()

        if not directory:
            return
        
        try:
            self.mainModel.set_top_directory(directory)
            self.mainView.set_directory_entry(directory)
            
        except ValueError as e:
            messagebox.showerror(title="Error", message=f"{e}")
    #Asks for files to add as attachments and updates view
    def add_attchment_button(self) -> None:
        files = filedialog.askopenfilenames()

        for file in files:
            self.mainView.add_attachment(file)
    #Removes selected attachment from view
    def remove_attachment_button(self) -> None:
        file_selection = self.mainView.attachmentsListBox.curselection()
        self.mainView.remove_attchment(file_selection)
    #Exit point for program after all data is input and saved
    #Updates items, attachments in model, creates file structure, generates log, and closes program
    def items_saved(self) -> None:

        rawItems: list[str] = []

        for item in self.itemView.entries:
            rawItems.append(item.get().strip())
        
        items = self.mainModel.update_items(rawItems)

        directory = self.mainView.directorySelectorEntry.get().strip() #Redundant fix
        
        self.mainModel.update_attachments(self.mainView.attachmentsListBox.get(0, tk.END))
        self.logfile.generate_log(
            self.fileCreator.create_file_structure(directory, self.mainModel.caseIdentifier, items, self.mainModel.attachmentList), 
            self.mainModel.caseIdentifier)

        self.mainView.root_window.destroy()
    #Gets item count from model for item view
    def get_item_count(self) -> int:
        return self.mainModel.itemNum # type: ignore
    
    def cyberTip_box_checked(self) -> None:
        print("Cybertip box checked")







        