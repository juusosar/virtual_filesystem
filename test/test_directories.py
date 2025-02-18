import unittest
from io import StringIO
from unittest.mock import patch
from main.core import MyVFS
from main.modules.node import MyVFSDir, MyVFSFile

class DirectoryTests(unittest.TestCase):
    def setUp(self):
        self.vfs = MyVFS()

    def test_create_dir(self):
        created_dir = self.vfs.create_directory("/juuso")

        self.assertIsInstance(created_dir, MyVFSDir)
        self.assertEqual(created_dir.name, "juuso")
        self.assertEqual(created_dir.parent_dir, self.vfs.root)

    def test_create_dir_multiple(self):
        created_dir1 = self.vfs.create_directory("/juuso")
        created_dir2 = self.vfs.create_directory("/kata")

        self.assertEqual(created_dir1.parent_dir, self.vfs.root)
        self.assertEqual(created_dir2.parent_dir, self.vfs.root)

    def test_create_dir_nested(self):
        parent_dir = self.vfs.create_directory("/juuso")
        child_dir1 = self.vfs.create_directory("/juuso/testi")
        child_dir2 = self.vfs.create_directory("/juuso/testi/keissit")

        self.assertEqual(parent_dir.parent_dir, self.vfs.root)
        self.assertEqual(child_dir1.parent_dir, parent_dir)
        self.assertEqual(child_dir2.parent_dir, child_dir1)

    def test_find_parent_dir(self):
        parent_dir = self.vfs.create_directory("/juuso")
        child_dir1 = self.vfs.create_directory("/juuso/testi")
        child_dir2 = self.vfs.create_directory("/juuso/testi/keissit")
        parent_dir, name = self.vfs._find_parent_dir("/juuso/testi/keissit")

        self.assertEqual(parent_dir, child_dir1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_list_directories_only_root(self, mock_output):
        self.vfs.list_directories()
        self.assertEqual(mock_output.getvalue().strip(), "/")

    @patch('sys.stdout', new_callable=StringIO)
    def test_list_directories_one(self, mock_output):
        self.vfs.create_directory("/juuso")
        self.vfs.list_directories()
        self.assertEqual(mock_output.getvalue().strip(), "/\n|juuso")

    @patch('sys.stdout', new_callable=StringIO)
    def test_list_directories_nested(self, mock_output):
        self.vfs.create_directory("/juuso")
        self.vfs.create_directory("/juuso/kuvat")
        self.vfs.create_directory("/juuso/testit")
        self.vfs.list_directories()
        self.assertEqual(mock_output.getvalue().strip(), "/\n|juuso\n||kuvat\n||testit")


if __name__ == '__main__':
    unittest.main()
