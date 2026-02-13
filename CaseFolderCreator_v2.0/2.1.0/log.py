from pathlib import Path

class Logger:

    def __init__(self):
        self.log: list[str] = []
        
    
    #Appends entry to log list
    def add_entry(self, data: str) -> None:
        self.log.append(data)
    
    #Generates log file at specified directory with specified filename
    def generate_log(self, directory, filename) -> None:
        filename = filename + ".txt"

        self.filepath = Path(directory).resolve()/filename

        with open(self.filepath, "a") as f:
            for entry in self.log:
                f.write(entry + "\n")
        
