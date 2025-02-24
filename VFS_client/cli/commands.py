import argparse

class CLICommands(object):

    @staticmethod
    def create_cd_parser():
        parser = argparse.ArgumentParser(prog="cd", description="Change active directory.")
        parser.add_argument("path", nargs="?", default=".", type=str,
                            help="Name or path to the directory to change to.")
        return parser

    @staticmethod
    def create_ls_parser():
        parser = argparse.ArgumentParser(prog="ls", description="List directory contents.")
        parser.add_argument("-t", "--tree", action="store_true",
                            help="Show directory contents as tree.")
        return parser

    @staticmethod
    def create_touch_parser():
        parser = argparse.ArgumentParser(prog="touch", description="Create a new file. ")
        parser.add_argument("path", nargs="?", default=".", type=str,
                            help="Name or path to the file to create.")
        parser.add_argument("-c", "--content", nargs="?", type=str,
                            help="Data to write to the created file.")
        return parser

    @staticmethod
    def create_mkdir_parser():
        parser = argparse.ArgumentParser(prog="mkdir", description="Create a new directory to the active directory.")
        parser.add_argument("path", nargs="?", default=".", type=str,
                            help="Path or of the directory to create.")
        return parser

    @staticmethod
    def create_rmdir_parser():
        parser = argparse.ArgumentParser(prog="rmdir", description="Remove an empty directory in the active directory.")
        parser.add_argument("path", nargs="?", default=".", type=str,
                            help="Path or name of the directory to remove.")
        return parser

    @staticmethod
    def create_pwd_parser():
        parser = argparse.ArgumentParser(prog="pwd", description="List the active directory.")
        return parser

    @staticmethod
    def create_cp_parser():
        parser = argparse.ArgumentParser(prog="cp", description="Copy a file or a directory.")
        parser.add_argument("source", nargs="?", default=".", type=str,
                            help="Source path to copy.")
        parser.add_argument("destination", nargs="?", default=".", type=str,
                            help="Destination directory where source is copied.")
        return parser

    @staticmethod
    def create_mv_parser():
        parser = argparse.ArgumentParser(prog="mv", description="Move a file or a directory.")
        parser.add_argument("source", nargs="?", default=".", type=str,
                            help="Source path to move.")
        parser.add_argument("destination", nargs="?", default=".", type=str,
                            help="Destination path where source is moved.")
        return parser

    @staticmethod
    def create_rm_parser():
        parser = argparse.ArgumentParser(prog="rm", description="Remove a file or a directory.")
        parser.add_argument("path", nargs="?", default=".", type=str,
                            help="Path to remove.")
        return parser

    @staticmethod
    def create_find_parser():
        parser = argparse.ArgumentParser(prog="find", description="Find file or directory address.")
        parser.add_argument("name", nargs="?", default=".", type=str,
                            help="Name of file to find")
        parser.add_argument("-d", "--directory", action="store_true",
                            help="If target is a directory.")
        return parser

    @staticmethod
    def create_cat_parser():
        parser = argparse.ArgumentParser(prog="cat", description="Read or write to file.\n"
                                                                 "Reads the file if you give only the path as an argument.")
        parser.add_argument("path", nargs="?", default=".", type=str,
                            help="Path of file to read or write to.")
        exclusive_commands = parser.add_mutually_exclusive_group()
        exclusive_commands.add_argument("-w", "--write", type=str,
                            help="Content to write to a file. Fails if file doesn't exist.")
        exclusive_commands.add_argument("-w+", "--overwrite", type=str,
                            help="Content to write to a file. Overwriting if it exists and create new if it doesn't.")
        exclusive_commands.add_argument("-a", "--append", type=str,
                            help="Content to append to a file.")
        return parser




