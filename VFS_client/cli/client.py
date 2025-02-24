#!/usr/bin/env python

from cmd import Cmd
from typing import IO
import shlex

import pyreadline3 as readline

from VFS_client import MyVFS, CLICommands


class CLI(Cmd, CLICommands):
    drive = '/'
    intro = 'CLI for an in-memory virtual unix-style filesystem.\nYou can list available commands by typing "?" and get more information by typing "help <command>"\n\nMounting filesystem drive...'
    prompt = f'{drive}>'

    def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None):
        super().__init__(completekey, stdin, stdout)
        self.vfs = None

        # Initialize all command parsers
        self.cd_parser = self.create_cd_parser()
        self.ls_parser = self.create_ls_parser()
        self.touch_parser = self.create_touch_parser()
        self.mkdir_parser = self.create_mkdir_parser()
        self.rmdir_parser = self.create_rmdir_parser()
        self.pwd_parser = self.create_pwd_parser()
        self.cp_parser = self.create_cp_parser()
        self.mv_parser = self.create_mv_parser()
        self.rm_parser = self.create_rm_parser()
        self.find_parser = self.create_find_parser()
        self.cat_parser = self.create_cat_parser()

    """
    Operative and configurative commands for the CLI application
    """
    def preloop(self):
        self.vfs = MyVFS()

    def postloop(self):
        # TODO: upload or save filesystem
        pass

    def do_exit(self, _):
        return True

    def help_exit(self):
        print("You can exit the program by typing in 'exit' or by pressing CTRL-D.")

    def update_prompt(self, active_dir):
        if active_dir == "":
            return
        self.prompt = f"{active_dir}>"

    do_EOF = do_exit
    help_EOF = help_exit

    """
    Custom cli commands for virtual filesystem
    """

    def do_test_env(self, args):
        self.vfs.create_test_env()

    """Change active directory"""
    def do_cd(self, args):
        try:
            parsed_args = self.cd_parser.parse_args(shlex.split(args))
            self.update_prompt(self.vfs.change_active_directory(parsed_args.path))
        except SystemExit:
            pass
        except SyntaxError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)

    def complete_cd(self, text, line, begidx, endidx):
        return [folder for folder in self.vfs.current.get_children_names() if folder.startswith(text)]

    def help_cd(self):
        self.cd_parser.print_help()

    """List directory contents"""
    def do_ls(self, args):
        try:
            parsed_args = self.ls_parser.parse_args(shlex.split(args))
            if parsed_args.tree:
                self.vfs.list_directories_and_files()
            else:
                self.vfs.list_current_directory()
        except SystemExit:
            pass
        except ValueError as e:
            print(e)

    def help_ls(self):
        self.ls_parser.print_help()

    """Create a new file or modify existing"""
    def do_touch(self, args):
        try:
            parsed_args = self.touch_parser.parse_args(shlex.split(args))
            self.vfs.create_file(parsed_args.path, content=parsed_args.content)
        except SystemExit:
            pass
        except SyntaxError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)

    def help_touch(self):
        self.touch_parser.print_help()

    """Create a new directory"""
    def do_mkdir(self, args):
        try:
            parsed_args = self.mkdir_parser.parse_args(shlex.split(args))
            self.vfs.create_directory(parsed_args.path)
        except SystemExit:
            pass
        except SyntaxError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)

    def help_mkdir(self):
        self.mkdir_parser.print_help()

    """Remove an empty directory"""
    def do_rmdir(self, args):
        try:
            parsed_args = self.rmdir_parser.parse_args(shlex.split(args))
            self.vfs.delete_directory(parsed_args.path)
        except SystemExit:
            pass
        except SyntaxError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)

    def help_rmdir(self):
        self.rmdir_parser.print_help()

    """Print current working directory"""
    def do_pwd(self, args):
        try:
            self.vfs.print_current_directory()
        except SystemExit:
            pass

    def help_pwd(self):
        self.pwd_parser.print_help()

    """Copy files or directories"""
    def do_cp(self, args):
        # TODO: Finish
        try:
            parsed_args = self.cp_parser.parse_args(shlex.split(args))
        except SystemExit:
            pass
        except SyntaxError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)

    def help_cp(self):
        self.cp_parser.print_help()

    """Move files or directories"""
    def do_mv(self, args):
        # TODO: Finish
        try:
            parsed_args = self.mv_parser.parse_args(shlex.split(args))
            if parsed_args.rename:
                self.vfs.rename_file(parsed_args.src, parsed_args.dest)
        except SystemExit:
            pass
        except SyntaxError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)

    def help_mv(self):
        self.mv_parser.print_help()

    """Remove files"""
    def do_rm(self, args):
        try:
            parsed_args = self.rm_parser.parse_args(shlex.split(args))
            self.vfs.delete_file(parsed_args.path)
        except SystemExit:
            pass
        except SyntaxError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)

    def help_rm(self):
        self.rm_parser.print_help()

    """Find file address"""
    def do_find(self, args):
        # TODO: Find file
        try:
            parsed_args = self.find_parser.parse_args(shlex.split(args))
            if parsed_args.directory:
                self.vfs.find_directory(parsed_args.directory)
            else:
                self.vfs.find_file(parsed_args.name)
        except SystemExit:
            pass
        except SyntaxError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)

    def help_find(self):
        self.find_parser.print_help()

    """Read and write files"""
    def do_cat(self, args):
        try:
            parsed_args = self.cat_parser.parse_args(shlex.split(args))
            if parsed_args.write:
                self.vfs.write_file(parsed_args.path, content=parsed_args.write, mode='w')
            elif parsed_args.overwrite:
                self.vfs.write_file(parsed_args.path, content=parsed_args.overwrite,mode='w+')
            elif parsed_args.append:
                self.vfs.write_file(parsed_args.path, content=parsed_args.append, mode='a')
            else:
                self.vfs.read_file(parsed_args.path)
        except SystemExit:
            pass
        except SyntaxError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)

    def complete_cat(self, text, line, begidx, endidx):
        return [file for file in self.vfs.current.get_filenames() if file.startswith(text)]

    def help_cat(self):
        self.cat_parser.print_help()


def run():
    readline.Readline().set_history_length(length=50) # Saves 50 previous inputs that can be navigated with UP/DOWN
    CLI().cmdloop()

if __name__ == "__main__":
    run()