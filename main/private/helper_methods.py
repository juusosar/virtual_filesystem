from main.modules.node import MyVFSDir, MyVFSFile

class VFSHelper(object):


    def _traverse_and_print(self, folder: MyVFSDir, prefix_line=""):
        for index, child in enumerate(folder.child_dirs.items()):
            name, child_obj = child
            last = index == len(folder.child_dirs) - 1
            symbol = '└──' if last else '├──'

            print(f"{prefix_line}{symbol}{name}")

            folder_line = '     ' if last else '│    '
            self._traverse_and_print(child_obj, prefix_line + folder_line)

    @staticmethod
    def _find_parent_dir(root: MyVFSDir, path: str) -> (MyVFSDir, str):
        path, name = path.rsplit("/", 1)
        path_parts = path.strip("/").split("/")
        parent = root
        for part in path_parts:
            if part in parent.child_dirs:
                parent = parent.child_dirs[part]
        return parent, name
