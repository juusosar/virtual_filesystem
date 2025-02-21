from typing import re

from VFS_client.src import MyVFSDir, MyVFSFile


class VFSHelper(object):


    def _traverse_and_print(self, folder: MyVFSDir, prefix_line="") -> None:
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

            folder_line = '     ' if last else '│    '
            self._traverse_and_print(child_obj, prefix_line + folder_line)

    def _find_file(self, root: MyVFSDir, path: str) -> MyVFSFile:
        if not "/" in path:
            return root.contents[path]

        if not self._check_path(path):
            raise SyntaxError("Invalid path")

        if result := self._traverse_directory_tree(root, path) is None:
            raise FileNotFoundError("Parent directory not found")

        parent, filename = result

        if file := parent.contents.get(filename) is None:
            raise FileNotFoundError("File not found")

        return file

    def _find_parent_dir(self, root: MyVFSDir, path: str) -> tuple[MyVFSDir, str] | None:
        """
        Finds the parent directory of a given path and extracts the target name from the path.

        :param root: Root directory object for the directory traversal.
        :param path: Path to traverse. Last item in the path assumed to be the target file/directory.
        :return: Directory object of the parent directory and the name of target directory/file as a tuple.
        """
        # Is given only the target name
        if not "/" in path:
            return root, path

        result = self._traverse_directory_tree(root, path)

        return result

    @staticmethod
    def _traverse_directory_tree(root: MyVFSDir, path: str) -> tuple[MyVFSDir, str] | None:
        """
        Traverses the directory tree to find the target object.

        :param root: Root directory object for the directory traversal.
        :param path: Path to traverse. Last item in the path assumed to be the target file/directory.
        :return: Parent directory object of the target object and the name of the target directory/file as a tuple.
        """
        path, name = path.rsplit("/", 1)
        path_parts = path.strip("/").split("/")
        parent = root
        for part in path_parts:
            if part in parent.child_dirs:
                parent = parent.child_dirs[part]

        if parent.name != path_parts[-1] and parent.name != root.name:
            return None

        return parent, name

    @staticmethod
    def _check_path(path: str) -> bool:
        """
        Checks if the given path is valid using regular expression.
        Following basic Unix-style file path naming scheme.

        Example: /home/user/juuso/testi.txt

        :param path: Path to be checked.
        :return: Boolean indicating if the path is valid.
        """
        absolute_regex_pattern = r'^\/(?:[^\/]+\/)*[^\/]*$'
        return bool(re.match(absolute_regex_pattern, path))
