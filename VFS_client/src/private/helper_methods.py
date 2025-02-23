import re
from datetime import datetime
from VFS_client.src import MyVFSDir, MyVFSFile

class VFSHelper(object):


    def _traverse_and_print(self, folder: MyVFSDir, prefix_line="", files=False) -> None:
        """
        Traverse the directory tree recursively and print the relations between the directories.

        :param folder: Start directory for the traversal.
        :param prefix_line: Prefix symbols to add in recursive executions.
        :return:
        """
        for index, child in enumerate(folder.child_dirs.items()):
            name, child_obj = child
            last = index == len(folder.child_dirs) - 1
            symbol = '└──' if last else '├──'

            print(f"{prefix_line}{symbol}{name}/")
            if files:
                for file in child_obj.get_filenames():
                    print(f"{prefix_line}{'│' if not last else ''}   {file}")

            folder_line = '     ' if last else '│    '
            self._traverse_and_print(child_obj, prefix_line + folder_line, files=files)

    def _find_file_by_path(self, root: MyVFSDir, path: str) -> MyVFSFile:
        if not "/" in path:
            return root.contents[path]

        if not self._is_valid_path(path):
            raise SyntaxError("Invalid path")

        result = self._find_parent_dir(root, path)
        if not result:
            raise FileNotFoundError("Parent directory not found")

        parent, filename = result
        file = parent.contents.get(filename)

        if not file:
            raise FileNotFoundError("File not found")

        return file

    def _find_file_by_name(self, root: MyVFSDir, name: str) -> MyVFSFile:
        # TODO: Search algorithm to find file in the system

        result = self._find_parent_dir(root, name)
        if not result:
            raise FileNotFoundError("Parent directory not found")

        parent, filename = result
        file = parent.contents.get(filename)

        if not file:
            raise FileNotFoundError("File not found")

        return file

    def _find_parent_dir(self, root: MyVFSDir, path: str, all_parents=False) -> tuple[MyVFSDir, str] | tuple[list[MyVFSDir], str]:
        """
        Finds the parent directory of a given path and extracts the target name from the path.

        :param root: Root directory object for the directory traversal.
        :param path: Path to traverse. Last item in the path assumed to be the target file/directory.
        :param all_parents: Flag to determine if only parent directory is returned
        :return: Directory object of the parent directory and the name of target directory/file as a tuple.

        :raises: FileNotFoundError: If any of the listed parent directories do not exist.
        """
        if not self._is_valid_path(path):
            raise SyntaxError("Invalid path")

        # Is given only the target name
        if not "/" in path:
            return root, path

        dir_path, name = path.rsplit("/", 1)
        parent_dirs = self._traverse_directory_tree(root, dir_path)

        if not parent_dirs:
            raise FileNotFoundError("Parent directory not found")

        if all_parents:
            return parent_dirs, name

        return parent_dirs[-1], name

    def _find_directory(self, root: MyVFSDir, path: str) -> MyVFSDir:
        folder = self._traverse_directory_tree(root, path)

        if not folder:
            raise FileNotFoundError("Directory not found")

        return folder[-1]


    @staticmethod
    def _construct_abs_path(directory: MyVFSDir) -> str:
        """
        Constructs the absolute path of a given directory by traversing upwards the directory tree.

        :param directory:
        :return: Absolute path to the given directory.
        """
        dir_list = [directory.name if directory.name != "/" else ""]
        parent = directory.parent_dir
        while parent:
            if parent.name == "/":
                break
            dir_list.insert(0, parent.name)
            parent = parent.parent_dir

        return f"/{'/'.join(dir_list)}"

    @staticmethod
    def _write_to_file(parent_dir: MyVFSDir, name: str, content: str, append=False) -> None:
        file: MyVFSFile = parent_dir.contents.get(name)

        if append: file.data += content
        else: file.data = content

        file.modified = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')
        file.set_size()
        parent_dir.set_size()

    @staticmethod
    def _traverse_directory_tree(root: MyVFSDir, path: str) -> list[MyVFSDir] | None:
        """
        Traverses the directory tree to find the target object.

        :param root: Root directory object for the directory traversal.
        :param path: Path to traverse. Last item in the path assumed to be the target file/directory.
        :return: List of parent directory objects of the target object and the name of the target directory/file as a tuple.
        """
        path_parts = path.strip("/").split("/")
        parent = root
        part_objs = [parent]
        for part in path_parts:
            if part in parent.child_dirs:
                parent = parent.child_dirs[part]
                part_objs.append(parent)

        if parent.name != path_parts[-1] and parent.name != root.name:
            return None

        return part_objs

    @staticmethod
    def _is_valid_path(path: str) -> bool:
        """
        Checks if the given path is a valid path or name using regular expression.
        Following basic Unix-style file path naming scheme.

        Example: /home/user/juuso/testi.txt

        :param path: Path to be checked.
        :return: Boolean indicating if the path is valid.
        """
        regex_pattern = r'^(\/(?:[^\/]+\/)*[^\/]+|[^\/]+|\.)$'
        return bool(re.match(regex_pattern, path))
