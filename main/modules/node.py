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
        self.created = self.modified = datetime.now()
        self.size = None

    def get_metadata(self):
        pass


class MyVFSDir(MyVFSNode):
    """
    Directory structure for virtual filesystem.

    Keeps list of the children directories and files in the directory both in a dictionary with names as keys and
    """

    def __init__(self, name, parent_dir):
        super().__init__(name, parent_dir)
        self.child_dirs: dict[str, MyVFSDir] = {}
        self.contents: dict[str, MyVFSFile] = {}

    def list_contents(self):
        pass


class MyVFSFile(MyVFSNode):
    """
    File structure for virtual filesystem.

    Data can be given either in bytes or string format. It is read into the I/O stream by using built-in io library
    and the reference to the stream object is saved in the file object.
    """
    def __init__(self, name: str, parent_dir: MyVFSDir, data: str):
        super().__init__(name, parent_dir)
        self.contents = data
