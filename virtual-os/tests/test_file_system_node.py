import unittest
from src.file_system_node import FileSystemNode

class TestFileSystemNode(unittest.TestCase):

    def test_directory_creation(self):
        node = FileSystemNode("test_dir")
        self.assertTrue(node.is_directory)
        self.assertEqual(node.name, "test_dir")

    def test_file_creation(self):
        node = FileSystemNode("test_file", is_directory=False)
        self.assertFalse(node.is_directory)
        self.assertEqual(node.name, "test_file")

if __name__ == '__main__':
    unittest.main()
