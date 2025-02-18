from main.modules.node import MyVFSDir, MyVFSFile
import private.helper_methods as _


class MyVFS:
    def __init__(self):
        self.root = MyVFSDir("/", parent_dir=None)
        self.current = self.root

    def create_file(self, path, content=""):
        parent_dir, name = _.find_parent_dir(self.root, path)

        parent_dir.contents[name] = MyVFSFile(name=name, parent_dir=parent_dir, data=content)

    def create_directory(self, path):
        parent_dir, name = _.find_parent_dir(self.root, path)

        new_dir = MyVFSDir(name=name, parent_dir=parent_dir)
        parent_dir.child_dirs[name] = new_dir

        return new_dir


    def move_file(self, source, destination):
        pass

    def copy_file(self, source, destination):
        pass

    def delete_file(self, path):
        pass

    def rename_file(self, path, new_path):
        pass

    def read_file(self, path):
        parent_dir, name = _.find_parent_dir(self.root, path)

    def write_file(self, path, content):
        pass

    def list_directories(self):
        print(f"{self.root.name}")
        _.recursive_dir_traversal(self.root, 0)


if __name__ == "__main__":
    vfs = MyVFS()
    vfs.create_directory("/juuso")
    vfs.create_directory("/kata")
    vfs.create_directory("/perhe")
    vfs.create_directory("/perhe/lapset")
    vfs.create_directory("/juuso/kuvat")
    vfs.create_directory("/juuso/testit")
    vfs.create_directory("/juuso/testit/keissit")
    vfs.list_directories()