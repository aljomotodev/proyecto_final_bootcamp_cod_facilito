from pathlib import Path

class fileAdmin():
    def __init__(self): 
        self.current_directory = Path.cwd()
        self.path = Path(self.current_directory)
        self.path_folder = self.path / 'scores'

        if not self.path_folder.exists():
            self.path_folder.mkdir() # Si la carpeta no existe, se procede a crear.
        
        self.path_file = self.path_folder / 'score.txt'

    def readFile(self):
        if self.path_file.is_file() and self.path_file.exists():
            return self.path_file.read_text()

    def writeFile(self, content):
        self.path_file.write_text(content)