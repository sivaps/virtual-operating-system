from file_system_node import FileSystemNode

class VirtualShell:
    def __init__(self):
        self.root = FileSystemNode("/")
        self.current_directory = self.root

    def list_directory(self):
        return ' '.join(child for child in self.current_directory.children.keys())

    def change_directory(self, path):
        if path in self.current_directory.children:
            self.current_directory = self.current_directory.children[path]
        else:
            print("Directory not found")

    def make_directory(self, name):
        if name not in self.current_directory.children:
            self.current_directory.children[name] = FileSystemNode(name)
        else:
            print("Directory already exists")

    def create_file(self, name):
        if name not in self.current_directory.children:
            self.current_directory.children[name] = FileSystemNode(name, is_directory=False)
        else:
            print("File already exists")
