import sys
from datetime import datetime


class MyVFSNode:
    """
    Node structure for the virtual file system.

    Directories are using a tree structure for good hierarchical representation of the system structure and fast traversal.

    Files ares stored in a dictionary with relation to the parent directory for fast file lookup and simplicity with large
    amounts of files.
    """
    def __init__(self, name: str, parent_dir):
        self.name = name
        self.parent_dir = parent_dir
        self.created = self.modified = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')
        self.size = 0

    def print_metadata(self):
        print(f"{self.name} - {self.size} bytes - {self.created} {f'- {self.modified}' if self.modified != self.created else ''}")



class MyVFSDir(MyVFSNode):
    """
    Directory structure for virtual filesystem.

    Keeps list of the children directories and files in the directory both in a dictionary with names as keys.
    """

    def __init__(self, name, parent_dir):
        super().__init__(name, parent_dir)
        self.child_dirs: dict[str, MyVFSDir] = {}
        self.contents: dict[str, MyVFSFile] = {}

    def list_all(self):
        self.list_children()
        self.list_files()

    def list_files(self):
        print("\nFiles:")
        for file in self.contents.values():
            file.print_metadata()

    def list_children(self):
        print("\nDirectories:")
        for folder in self.child_dirs.values():
            folder.print_metadata()

    def get_filenames(self):
        return [file for file in self.contents.keys()]

    def get_children_names(self):
        return [folder for folder in self.child_dirs.keys()]

    def set_size(self):
        self.size = 0
        for file in self.contents.values():
            self.size += file.size
        for folder in self.child_dirs.values():
            self.size += folder.set_size()

        return self.size


class MyVFSFile(MyVFSNode):
    """
    File structure for virtual filesystem.

    Data can be given either in bytes or string format. It is read into the I/O stream by using built-in io library
    and the reference to the stream object is saved in the file object.
    """
    def __init__(self, name: str, parent_dir: MyVFSDir, data: str):
        super().__init__(name, parent_dir)
        self.data = data
        self.size = sys.getsizeof(data)

    def set_size(self):
        self.size = sys.getsizeof(self.data)
