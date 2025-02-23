import unittest
from VFS_client import MyVFS


class FileTests(unittest.TestCase):
    def setUp(self):
        self.vfs = MyVFS()
        self.vfs.create_directory("/test")

    def test_create_file(self):
        self.vfs.create_file("/test/test.txt", "Hello World!")
        self.assertEqual(self.vfs.read_file("/test/test.txt"), "Hello World!")

    def test_create_file_to_root(self):
        self.vfs.create_file("test.txt", "Hello World!")
        self.assertEqual(self.vfs.read_file("test.txt"), "Hello World!")

    def test_create_file_fail(self):
        self.assertRaises(FileNotFoundError, self.vfs.create_file, "/test/eiole/test.txt", "Hello World!")

    def test_read_file(self):
        self.vfs.create_file("/test/test.txt", "Hello World!")
        self.assertEqual(self.vfs.read_file("/test/test.txt"), "Hello World!")





if __name__ == '__main__':
    unittest.main()
