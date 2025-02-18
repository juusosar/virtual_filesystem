from main.modules.node import MyVFSDir, MyVFSFile



def recursive_dir_traversal(folder: MyVFSDir, iteration: int):
    for name, child in folder.child_dirs.items():
        print(f"|{'|-'*iteration}{name}")
        recursive_dir_traversal(child, iteration+1)

def find_parent_dir(root: MyVFSDir, path: str) -> (MyVFSDir, str):
    path, name = path.rsplit("/", 1)
    path_parts = path.strip("/").split("/")
    parent = root
    for part in path_parts:
        if part in parent.child_dirs:
            parent = parent.child_dirs[part]
    return parent, name

def find_file_by_name(self, name: str) -> MyVFSFile:
    pass