class TextDocument:
    """Загружает текст из .txt файла"""

    def __init__(self):
        self.text = ""
        self.filename = ""

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text = file.read()
            self.filename = file_path
            return True
        except FileNotFoundError:
            print(f"Error: File {file_path} not found")
            return False
        except Exception as e:
            print(f"Error reading file: {e}")
            return False

    def get_text(self):
        return self.text

    def get_filename(self):
        return self.filename

