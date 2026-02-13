import tkinter as tk

from tkinter import BooleanVar, messagebox, filedialog

from main_view import MainView, ItemView

from main_model import MainModel

from file_creator import FileCreator
from log import Logger

#from settings_controller import PreferencesController
#from settings_model import PreferencesModel
#from settings_view import PreferencesView

#Controller for entire program

class MainController:

    def __init__(self):
        self.logfile = Logger()
        self.mainModel = MainModel(self.logfile)
        self.root_window = tk.Tk()
        self.mainView = MainView(self.root_window, self)
        self.CybertipBoxFlag: BooleanVar = tk.BooleanVar()

        self.fileCreator = (FileCreator(self.logfile))

    def run(self) -> None:
        self.mainView.run()

    #Retrieves and updates model with data input in GUI
    def continue_button_clicked(self) -> None:
        if self.getCyberTipStatus():
            self.continue_button_clicked_bypass_items()
            return
        if self.mainModel.bypassItems:
            self.continue_button_clicked_bypass_items()
            return

        caseNumber = self.mainView.caseNumberEntry.get().strip()
        caseAgent = self.mainView.agentEntry.get().strip()
        lineItems = self.mainView.itemNumEntry.get()
        directory = self.mainView.directorySelectorEntry.get().strip()

        try:
            self.mainModel.update_case_info(caseNumber, caseAgent, lineItems, directory)
        except (ValueError, FileExistsError) as e:
            messagebox.showerror(title="Error", message=f"{e}")
            return
        
        self.itemView = ItemView(self.root_window, self)
    
    def continue_button_clicked_bypass_items(self):
        caseNumber = self.mainView.caseNumberEntry.get().strip()
        caseAgent = self.mainView.agentEntry.get().strip()
        directory = self.mainView.directorySelectorEntry.get().strip()

        try:
            self.mainModel.update_case_info(caseNumber, caseAgent, "0", directory)
        except (ValueError, FileExistsError) as e:
            messagebox.showerror(title="Error", message=f"{e}")
            return
        
        directory = self.mainView.directorySelectorEntry.get().strip() #Redundant fix
        
        self.mainModel.update_attachments(self.mainView.attachmentsListBox.get(0, tk.END))

        if self.getCyberTipStatus() == True:        
            self.logfile.generate_log(
                self.fileCreator.create_cybertip_structure(directory, self.mainModel.caseIdentifier, self.mainModel.attachmentList, self.mainView.hashComboBox.get()),
                self.mainModel.caseIdentifier)
        if self.mainModel.bypassItems == True:        
            self.logfile.generate_log(
                self.fileCreator.create_bypass_items_structure(directory, self.mainModel.caseIdentifier, self.mainModel.attachmentList, self.mainView.hashComboBox.get()),
                self.mainModel.caseIdentifier)
        else:
            raise ValueError("FATAL ERROR: Bypass items or CyberTip flag not set correctly.")
        
        self.mainView.root_window.destroy()
        
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
            self.fileCreator.create_file_structure(directory, self.mainModel.caseIdentifier, items, self.mainModel.attachmentList, self.mainModel.isCyberTip, self.mainView.hashComboBox.get(), self.mainModel.bypassItems), 
            self.mainModel.caseIdentifier)
        
        self.mainView.root_window.destroy()

    def settings_button_clicked(self) -> None:
        pass
        
        #self.settingsController = PreferencesController(self.logfile)
        #self.settingsView = PreferencesView(self.root_window, self.settingsController)

    #Gets item count from model for item view
    def get_item_count(self) -> int:
        return self.mainModel.itemNum # type: ignore
    
    def cyberTip_box_checked(self) -> None:
        self.mainModel.isCyberTip = self.mainView.CybertipBoxFlag.get()

        if self.mainModel.isCyberTip:
            self.mainView.itemNumEntry.delete(0, tk.END)
            self.mainView.itemNumEntry.config(state='disabled')

            self.mainView.caseNumberLabel.config(text="CyberTip Number")
            self.mainView.agentLabel.config(text="Electronic Service Provider (ESP)")
        else:
            self.mainView.itemNumEntry.config(state='normal')
            self.mainView.caseNumberLabel.config(text="Case Number")
            self.mainView.agentLabel.config(text="Agent")
            
    def bypass_items(self) -> None:
        self.mainModel.bypassItems = self.mainView.bypassItemsFlag.get()

        if self.mainModel.bypassItems:
            self.mainView.itemNumEntry.delete(0, tk.END)
            self.mainView.itemNumEntry.config(state='disabled')
        else:
            self.mainView.itemNumEntry.config(state='normal')
    
    def getCyberTipStatus(self) -> bool:
        return self.mainModel.isCyberTip
    
    def update_progress_label(self, text: str) -> None:
        self.mainView.progressLabel.config(text=text)
    







        