from datetime import datetime
from VFS_client.src import MyVFSDir, MyVFSFile, VFSHelper

class MyVFS(VFSHelper):

    def __init__(self):
        self.root = MyVFSDir('/', parent_dir=None)
        self.current = self.root

    def change_active_directory(self, path: str) -> str:
        """
        Changes the active directory to the given path.

        If path is empty or '.', doesn't do anything.

        :param path: Path (or directory name if subdirectory) to change the active directory to.
        :return:
        """
        match path:
            case '.' | '' | self.current.name:
                return ''

            case '..' | '../':
                # FIXME: Jos on usea peräkkäin. CLI clienttiin?
                if not self.current.parent_dir:
                    return ''
                self.current = self.current.parent_dir
                return self._construct_abs_path(self.current)

            case _:
                if not self._is_valid_path(path):
                    raise SyntaxError("Invalid path")

                if path in self.current.child_dirs:
                    self.current = self.current.child_dirs[path]
                    return self._construct_abs_path(self.current)

                self.current = self._find_directory(self.current, path)
                return self._construct_abs_path(self.current)

    def print_current_directory(self):
        print(self._construct_abs_path(self.current))

    def create_file(self, path: str, content: str=None) -> MyVFSFile:
        """
        Creates a file in the filesystem with the supplied path and content.

        :param path: Path to the file. If given just a name, creates a file in the root directory
        :param content: File content to write to the file. Defaults to empty.
        :return: The created file object.

        :raises FileNotFoundError: If supplied parent directory does not exist.
        :raises SyntaxError: If given path is not valid.
        """
        parent_dir, name = self._find_parent_dir(self.current, path)
        print("Name of created file:", name)

        new_file = MyVFSFile(name=name, parent_dir=parent_dir, data=content)
        parent_dir.contents[name] = new_file
        parent_dir.set_size()

        return new_file


    def create_directory(self, path: str) -> MyVFSDir:
        """
        Creates a directory with the supplied path.

        :param path: Path to the directory. If given just a name, creates a directory in the root directory.
        :return: The created directory object.

        :raises FileNotFoundError: If supplied parent directory does not exist.
        :raises SyntaxError: If given path is not valid.
        """
        parent_dir, name = self._find_parent_dir(self.current, path)

        new_dir = MyVFSDir(name=name, parent_dir=parent_dir)
        parent_dir.child_dirs[name] = new_dir

        return new_dir

    def delete_directory(self, path: str) -> None:
        # TODO
        pass

    def move_file(self, source_path: str, destination_path: str):
        # TODO
        pass

    def copy_file(self, source_path: str, destination_path: str):
        # TODO
        pass

    def delete_file(self, path: str) -> None:
        """
        Deletes the supplied file from the filesystem.

        :param path: Path to delete the file from.
        :return:

        :raises FileNotFoundError: If supplied file can't be found.
        :raises SyntaxError: If given path is not valid.
        """
        parent_dir, name = self._find_parent_dir(self.current, path)

        if not parent_dir.contents.get(name):
            raise FileNotFoundError("File does not exist")

        del parent_dir.contents[name]
        parent_dir.set_size()

    def rename_file(self, path: str, new_name: str) -> None:
        """
        Renames the supplied file and it's references.

        :param path: Path to the file to be renamed
        :param new_name: New name for the file.
        :return:

        :raises FileNotFoundError: If supplied file can't be found.
        :raises SyntaxError: If given path is not valid.
        """
        parent_dir, name = self._find_parent_dir(self.current, path)

        if not parent_dir.contents.get(name):
            raise FileNotFoundError("File does not exist")

        file_obj: MyVFSFile = parent_dir.contents.get(name)
        file_obj.name = new_name
        file_obj.modified = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')

        parent_dir[new_name] = parent_dir.pop(name)

    def read_file(self, path: str) -> None:
        """
        Read file contents.

        :param path: Path to the file to read.

        :raises FileNotFoundError: If supplied file can't be found.
        :raises SyntaxError: If given path is not valid.
        """
        parent_dir, name = self._find_parent_dir(self.current, path)

        if not parent_dir.contents.get(name):
            raise FileNotFoundError("File does not exist")

        print(parent_dir.contents.get(name).data)
        return parent_dir.contents.get(name).data

    def write_file(self, path: str, content: str, mode: str='w') -> None:
        """
        Writes content to the file depending on the mode.

        :param path: Name or path to the file.
        :param content: Data to write to the file.
        :param mode:
            w -> write to existing file, fail if it doesn't exist
            w+ -> write to new file, overwrite if exists
            a -> append to existing file

        :raises FileNotFoundError: If supplied file can't be found.
        :raises SyntaxError: If given path is not valid.
        """
        parent_dir, name = self._find_parent_dir(self.current, path)

        match mode:
            case 'w':
                if not parent_dir.contents.get(name):
                    raise FileNotFoundError("File does not exist")
                self._write_to_file(parent_dir, name, content)
                return

            case 'w+':
                if not parent_dir.contents.get(name):
                    self.create_file(path, content)
                    return
                self._write_to_file(parent_dir, name, content)
                return

            case 'a':
                if not parent_dir.contents.get(name):
                    raise FileNotFoundError("File does not exist")
                self._write_to_file(parent_dir, name, content, append=True)
                return

    def file_exists(self, path: str) -> bool:
        """
        Checks if the supplied file exists.

        :param path: Path to the file to check.
        :return:
        """
        # I don't like this approach, but I'll go with it for now
        try:
            self._find_file_by_path(self.root, path)
            return True
        except FileNotFoundError:
            return False

    def list_current_directory(self):
        """
        Lists current directory contents with metadata.
        """
        self.current.list_all()

    def list_directories(self) -> None:
        """
        Lists all directories in the filesystem as a tree structure using active directory as root.
        """
        self._traverse_and_print(self.current)

    def list_directories_and_files(self) -> None:
        """
        Lists all directories and files in the filesystem using active directory as root.
        """
        print("root:")
        self._traverse_and_print(self.current, files=True)

    def reset(self) -> None:
        self.__init__()

    def create_test_env(self):
        """
        Create a test environment quickly
        """
        self.create_directory("/test")
        self.create_directory("/test/tests")
        self.create_directory("/test/tests/cases")
        self.create_file("/test/tests/cases/testcase1.txt", "This is a test case and it's number is 1")
        self.create_directory("/test/tests/cases/fails")
        self.create_directory("/lorem")
        self.create_directory("/lorem/ipsum")
        self.create_directory("/lorem/ipsum/dolor")
        self.create_file("/lorem/ipsum/dolor/sit.amet", "lorem ipsum dolor sit amet")
        self.create_directory("/misc")
        self.create_file("/misc/data.enc", "encrypted_data")
        self.list_directories_and_files()


if __name__ == "__main__":
    vfs = MyVFS()
    vfs.create_test_env()