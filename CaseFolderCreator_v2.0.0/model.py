import os

class MainModel:

    def __init__(self, logfile):
        self.caseNumber: str | None = None
        self.agent: str | None = None
        self.caseIdentifier: str | None = None
        self.itemNum: int | None = None
        self.topDirectory: str | None = None
        self.isCyberTip: bool = False

        self.logfile=logfile

        self.items: list[str] = []
        self.attachmentList: list[str] = []
        self.attachmentHashes: dict[str, str] = {}

    def concatenate_case_identifier(self, caseNumber: str, agent: str) -> None:
        self.caseIdentifier = (caseNumber + '_' + agent)

    def update_case_info(self, caseNumber: str, agent: str, itemNum: str, topDirectory: str) -> None:

        if not caseNumber:
            raise ValueError("Case Number cannot be empty")
        if not agent:
            raise ValueError("Agent cannot be empty")
        if not itemNum:
            raise ValueError("Line Items cannot be empty")
        if not topDirectory:
            raise ValueError("Case Folder Location cannot be empty")

        self.caseNumber = caseNumber
        self.agent = agent
        self.itemNum = int(itemNum)
        self.topDirectory = topDirectory

        self.concatenate_case_identifier(caseNumber, agent)

        self.logfile.add_entry(f"Case number: {self.caseNumber}")
        self.logfile.add_entry(f"Agent: {self.agent}")
        self.logfile.add_entry(f"Identifier:{self.caseIdentifier}")
        self.logfile.add_entry(f"Number of line items:{self.itemNum}")
        self.logfile.add_entry(f"Directory: {self.topDirectory}\n")

    def set_top_directory(self, directory: str) -> None:

        if not os.path.isdir(directory):
            raise ValueError("Selected path is not a directory")
        
        self.topDirectory = directory

    def update_items(self, itemList: list[str]) -> list[str]:
        
        self.items = [item.strip() for item in itemList if item.strip()]
        self.logfile.add_entry(f"Item list: {itemList}")
        return self.items
    
    def update_attachments(self, attachments: list[str]) -> list[str]:
        self.attachmentList = [attc.strip() for attc in attachments if attc.strip()]

        for attc in self.attachmentList:
            self.logfile.add_entry(f"Attachment: {attc}")
        return self.attachmentList

    #def set_cybertip_flag(self, val: bool) -> None:
        #self.isCyberTip = val
        #print(f"Cybertip: {val}")
        
        
            