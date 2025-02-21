from cmd import Cmd
from typing import IO
from VFS_client import MyVFS

class CLI(Cmd):
    drive = '/'
    intro = 'CLI for an in-memory virtual unix filesystem.\n\nMounting filesystem drive...'
    prompt = f'{drive}>'

    def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None):
        super().__init__(completekey, stdin, stdout)
        self.vfs = None

    """
    Operative and configurative commands for the CLI application
    """
    def preloop(self):
        self.vfs = MyVFS(f"{self.drive}")

    def postloop(self):
        pass

    def do_help(self, args):
        pass

    def do_exit(self, args):
        pass

    def help_exit(self):
        pass

    def update_prompt(self, active_dir):
        # FIXME: vaihtaa promptin oikein
        self.prompt = f"{self.drive}/{active_dir}>"

    do_EOF = do_exit
    help_EOF = help_exit

    """
    Custom cli commands for virtual filesystem
    """
    # Change active directory
    def do_cd(self, args):
        if args == "":
            print(self.vfs.current.name)
        else:
            self.update_prompt(self.vfs.change_active_directory(args))

    def help_cd(self):
        pass

    # List directory contents
    def do_ls(self, args):
        self.vfs.list_directories()

    def help_ls(self):
        pass

    # Create a new file or modify existing
    def do_touch(self, args):
        self.vfs.create_file(args)

    def help_touch(self):
        pass

    # Create a new directory
    def do_mkdir(self, args):
        self.vfs.create_directory(args)

    def help_mkdir(self):
        pass

    # Remove an empty directory
    def do_rmdir(self, args):
        pass

    def help_rmdir(self):
        pass

    # Print current working directory
    def do_pwd(self, args):
        pass

    def help_pwd(self):
        pass

    # Copy files or directories
    def do_cp(self, args):
        pass

    def help_cp(self):
        pass

    # Move files or directories
    def do_mv(self, args):
        pass

    def help_mv(self):
        pass

    # Remove files or directories
    def do_rm(self, args):
        pass

    def help_rm(self):
        pass


def run():
    CLI().cmdloop()

if __name__ == "__main__":
    run()