import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class MainView:

    def __init__(self, root, controller):

        #Root Window
        self.root_window = root
        self.controller = controller

        self.CybertipBoxFlag: tk.BooleanVar = tk.BooleanVar()
        self.bypassItemsFlag: tk.BooleanVar = tk.BooleanVar()

        self.hashComboBoxOptions = ["MD5", "SHA1", "SHA256"]

        self._build_ui()
    
    def _build_ui(self) -> None:
        self.root_window.columnconfigure(0, weight=1)
        self.root_window.columnconfigure(1, weight=1)
        self.root_window.columnconfigure(2, weight=1)
        self.root_window.title("Case Folder Creator")

        case_frame = ttk.LabelFrame(self.root_window, text="Case Information", padding=15)
        case_frame.grid(row=0, column=0, columnspan=3, sticky="ew", padx=15, pady=10)

        self.caseNumberLabel = ttk.Label(case_frame, text="Case Number")
        self.caseNumberLabel.grid(row=0, column=0, sticky="w")
        self.caseNumberEntry = ttk.Entry(case_frame, width=20)
        self.caseNumberEntry.grid(row=1, column=0, padx=5, pady=(0, 10))

        self.agentLabel = ttk.Label(case_frame, text="Case Agent (Last Name)")
        self.agentLabel.grid(row=0, column=1, sticky="w")
        self.agentEntry = ttk.Entry(case_frame, width=20)
        self.agentEntry.grid(row=1, column=1, padx=5, pady=(0, 10))

        ttk.Label(case_frame, text="Line Items").grid(row=0, column=2, sticky="w")
        self.itemNumEntry = ttk.Entry(case_frame, width=5)
        self.itemNumEntry.grid(row=1, column=2, padx=5, pady=(0, 10))

        options_frame = ttk.LabelFrame(self.root_window, text="Options", padding=15)
        options_frame.grid(row=1, column=0, columnspan=3, sticky="ew", padx=15, pady=10)

        ttk.Label(options_frame, text="Case Folder Location").grid(row=0, column=0, sticky="w")
        self.directorySelectorEntry = ttk.Entry(options_frame, width=50)
        self.directorySelectorEntry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)

        ttk.Button(options_frame, text="Browse…", command=self.controller.directory_button_clicked).grid(row=1, column=2, padx=5)

        ttk.Label(options_frame, text="Hash Type").grid(row=2, column=0, sticky="w", pady=(10, 0))
        self.hashComboBox = ttk.Combobox(options_frame, values=self.hashComboBoxOptions, width=10, state="readonly")
        self.hashComboBox.current(0)  # Default to MD5
        self.hashComboBox.grid(row=3, column=0, sticky="w")

        self.isCybertipCheckbox = ttk.Checkbutton(
            options_frame,
            text="Cybertip",
            variable=self.CybertipBoxFlag,
            command=self.controller.cyberTip_box_checked)
        
        self.isCybertipCheckbox.grid(row=3, column=1, sticky="w")

        self.bypassItemEntryCheckbox = ttk.Checkbutton(
            options_frame,
            text="Bypass Line Items Entry",
            variable=self.bypassItemsFlag,
            command=self.controller.bypass_items)
        self.bypassItemEntryCheckbox.grid(row=3, column=2, sticky="w")

        attachments_frame = ttk.LabelFrame(self.root_window, text="Attachments", padding=15)
        attachments_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=15, pady=10)

        self.attachmentsListBox = tk.Listbox(attachments_frame, height=6, width=50)
        self.attachmentsListBox.grid(row=0, column=0, columnspan=2, sticky="ew")

        ttk.Button(
            attachments_frame,
            text="Add",
            command=self.controller.add_attchment_button
        ).grid(row=1, column=0, pady=5)

        ttk.Button(
            attachments_frame,
            text="Remove",
            command=self.controller.remove_attachment_button
        ).grid(row=1, column=1, pady=5)

        action_frame = ttk.Frame(self.root_window)
        action_frame.grid(row=3, column=0, columnspan=3, sticky="ew", padx=15, pady=10)

        ttk.Button(
            action_frame,
            text="Continue",
            command=self.controller.continue_button_clicked
        ).pack(side="right")

        ttk.Button(
            action_frame,
            text="Settings",
            command=self.controller.settings_button_clicked,
            state="disabled"
        ).pack(side="left")

        # Status bar
        self.progressLabel = ttk.Label(
            self.root_window,
            text="Ready",
            anchor="w",
            relief="sunken",
            padding=5
        )
        self.progressLabel.grid(row=4, column=0, columnspan=3, sticky="ew")


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
            messagebox.showwarning(title="Warning", message="Please select an attachment to remove.")
            return
    
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
            entry.grid(row=i + 1, column=0, padx=5, pady=5)
            self.entries.append(entry)
        
        saveButton = tk.Button(self.window, text='Save', command = self.controller.items_saved)
        saveButton.grid(pady=10)





