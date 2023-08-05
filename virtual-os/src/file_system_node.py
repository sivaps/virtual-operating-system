class FileSystemNode:
    def __init__(self, name, is_directory=True):
        self.name = name
        self.is_directory = is_directory
        self.children = {} if is_directory else None
