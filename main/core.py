from datetime import datetime
from main.modules.node import MyVFSDir, MyVFSFile
from main.private.helper_methods import VFSHelper


class MyVFS(VFSHelper):

    def __init__(self, root_dir_name: str):
        self.root = MyVFSDir(root_dir_name, parent_dir=None)
        self.current = self.root

    def create_file(self, path: str, content: str="") -> MyVFSFile:
        parent_dir, name = self._find_parent_dir(self.root, path)
        print("Name of created file:", name)

        new_file = MyVFSFile(name=name, parent_dir=parent_dir, data=content)
        parent_dir.contents[name] = new_file

        return new_file


    def create_directory(self, path: str) -> MyVFSDir:
        parent_dir, name = self._find_parent_dir(self.root, path)

        new_dir = MyVFSDir(name=name, parent_dir=parent_dir)
        parent_dir.child_dirs[name] = new_dir

        return new_dir

    def move_file(self, source_path: str, destination_path: str):
        pass

    def copy_file(self, source_path: str, destination_path: str):
        pass

    def delete_file(self, path: str) -> None:
        parent_dir, name = self._find_parent_dir(self.root, path)

        parent_dir.contents.pop(name)

    def rename_file(self, path: str, new_name: str) -> None:
        parent_dir, name = self._find_parent_dir(self.root, path)

        file_obj = parent_dir.contents[name]
        file_obj.name = new_name
        file_obj.modified = datetime.now()

    def read_file(self, path: str):
        parent_dir, name = self._find_parent_dir(self.root, path)

        print("Data from the file:", parent_dir.contents[name].data)
        return parent_dir.contents[name].data

    def write_file(self, path: str, content: str, mode: str='w') -> None:
        """

        :param path:
        :param content:
        :param mode:
            w -> write to existing file, fail if it doesn't exist
            w+ -> write to new file, overwrite existing file
            a -> append to existing file
            a+ -> append to new file
        :return:
        """
        parent_dir, name = self._find_parent_dir(self.root, path)

        file_obj = parent_dir.contents[name]
        file_obj.data = content
        file_obj.modified = datetime.now()

    def list_directories(self) -> None:
        print(f"{self.root.name}")
        self._traverse_and_print(self.root)


if __name__ == "__main__":
    vfs = MyVFS("VFS:")
    vfs.create_directory("/juuso")
    vfs.create_directory("/kata")
    vfs.create_directory("/perhe")
    vfs.create_directory("/perhe/lapset")
    vfs.create_directory("/juuso/kuvat")
    vfs.create_directory("/juuso/testit")
    vfs.create_directory("/juuso/testit/keissit")
    vfs.create_directory("/juuso/testit/feilit")
    vfs.create_directory("/juuso/kokeet")
    vfs.list_directories()