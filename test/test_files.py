import unittest
from main.core import MyVFS


class FileTests(unittest.TestCase):
    def setUp(self):
        self.vfs = MyVFS()

    def test_create_file(self):
        self.vfs.create_file("/juuso/test.txt", "Hello World!")
        self.assertEqual(self.vfs.read_file("/juuso/text.txt"), "Hello World!")

    def test_read_file(self):
        self.vfs.create_file("/juuso/test.txt", "Hello World!")
        self.assertEqual(self.vfs.read_file("/juuso/test.txt"), "Hello World!")



if __name__ == '__main__':
    unittest.main()
