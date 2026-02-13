from pathlib import Path
from docx import Document as Doc

import shutil

from hasher import Hasher


#Logic for file structure creator. Heavily reworked.

class FileCreator:

    def __init__(self, logfile):
        self.SUB_DIRS = ['img', 'reports', 'exam_photos']
        self.tipLevelOne = ['cybertip', 'intel', 'legal']
        self.cybertipSubdirs = ['CSAM']
        self.legalSubdirs = ['SDT', 'SW']
        self.attachmentList: list[str] = []
                                
        self.topDir: Path
        self.logfile = logfile

    #Creates file structure based on inputs from model
    def create_file_structure(self, rootDirectory, caseIdentifier, items, attachments, isCyberTip, hash_algorithm, bypassItems):
        hasher = Hasher(workers=4, algorithm=hash_algorithm)

        self.load_attachments(attachments)

        if isCyberTip:
            return self.create_cybertip_structure(rootDirectory, caseIdentifier, attachments, hash_algorithm)
        
        if bypassItems:
            return self.create_bypass_items_structure(rootDirectory, caseIdentifier, attachments, hash_algorithm)

        root = Path(rootDirectory).resolve()

        if not root.is_dir():
            raise ValueError("Base directory is invalid")

        top = root / caseIdentifier
        doc_path = top / f"{caseIdentifier}.docx"
        report_doc = Doc()
        
        if top.exists():
            raise FileExistsError(f"Case folder already exists: {top}")
        self._mkdir(top)

        report_doc.save(doc_path)

        for item in items:
            item_dir = top / item
            self._mkdir(item_dir)

            for sub_dir in self.SUB_DIRS:
                self._mkdir(item_dir / sub_dir)
        
        for attc in attachments:
            resolved_attc = Path(attc).resolve()

            if not resolved_attc.is_file():
                raise ValueError(f"Attachment {attc} is invalid")
            
            shutil.copy2(attc, top)
        
        hashes = hasher.hash_files(attachments)

        for path, digest in hashes.items():
            self.logfile.add_entry(f"Hashed {path.name}: {digest}")
        return top


     
    def create_cybertip_structure(self, rootDirectory, caseIdentifier, attachments, hash_algorithm):
        self.load_attachments(attachments)

        hasher = Hasher(workers=4, algorithm=hash_algorithm)

        root = Path(rootDirectory).resolve()

        if not root.is_dir() or not root.is_dir():
            raise ValueError("Base directory is invalid")
        
        top = root / caseIdentifier

        if top.exists():
            raise FileExistsError(f"Case folder already exists: {top}")
        self._mkdir(top)

        for subdir in self.tipLevelOne:
            self._mkdir(top / subdir)

        for attc in attachments:
            resolved_attc = Path(attc).resolve()

            if not resolved_attc.is_file():
                raise ValueError(f"Attachment {attc} is invalid")
            
            shutil.copy2(attc, top)

        hashes = hasher.hash_files(attachments)

        for path, digest in hashes.items():
            self.logfile.add_entry(f"Hashed {path.name}: {digest}")
            
        return top
    
    def create_bypass_items_structure(self, rootDirectory, caseIdentifier, attachments, hash_algorithm):
        self.load_attachments(attachments)

        hasher = Hasher(workers=4, algorithm=hash_algorithm)

        root = Path(rootDirectory).resolve()

        if not root.is_dir() or not root.is_dir():
            raise ValueError("Base directory is invalid")
        
        top = root / caseIdentifier

        if top.exists():
            raise FileExistsError(f"Case folder already exists: {top}")
        self._mkdir(top)

        for attc in attachments:
            resolved_attc = Path(attc).resolve()

            if not resolved_attc.is_file():
                raise ValueError(f"Attachment {attc} is invalid")
            
            shutil.copy2(attc, top)

        hashes = hasher.hash_files(attachments)

        for path, digest in hashes.items():
            self.logfile.add_entry(f"Hashed {path.name}: {digest}")
            
        return top

    #Makes directory and logs creation
    def _mkdir(self, path: Path) -> None:
        path.mkdir(exist_ok=True) #I don't like this but it works for now
        self.logfile.add_entry(f"Created {path}")

    

    def load_attachments(self, attachments: list[str]) -> None:
        self.attachmentList = [attc.strip() for attc in attachments if attc.strip()]
        
        
