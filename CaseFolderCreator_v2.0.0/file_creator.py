from pathlib import Path
from docx import Document as Doc
import shutil
import hashlib

#Logic for file structure creator. Heavily reworked.

class FileCreator:

    def __init__(self, logfile):
        self.SUB_DIRS = ['img', 'reports', 'exam_photos']
        self.topDir: Path
        self.logfile = logfile

    #Creates file structure based on inputs from model
    def create_file_structure(self, rootDirectory, caseIdentifier, items, attachments) -> Path:

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
            attc_hash = self._hash_file(resolved_attc)
            self.logfile.add_entry("\nHashed {attc}: {attc_hash}")
        
        return top


    #Makes directory and logs creation 
    def _mkdir(self, path: Path) -> None:
        path.mkdir(exist_ok=True) #I don't like this but it works for now
        self.logfile.add_entry(f"Created {path}")
    
    #Hashes file for integrity logging
    def _hash_file(self, file: Path) -> str:
        hash_md5 = hashlib.md5()

        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hash_md5.update(chunk)
        
        return hash_md5.hexdigest()
        
