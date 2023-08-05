import unittest
from src.virtual_shell import VirtualShell

class TestVirtualShell(unittest.TestCase):

    def setUp(self):
        self.shell = VirtualShell()

    def test_list_directory(self):
        self.assertEqual(self.shell.list_directory(), '')

    def test_make_directory(self):
        self.shell.make_directory('test_dir')
        self.assertIn('test_dir', self.shell.current_directory.children)

    def test_create_file(self):
        self.shell.create_file('test_file')
        self.assertIn('test_file', self.shell.current_directory.children)

    def test_change_directory(self):
        self.shell.make_directory('test_dir')
        self.shell.change_directory('test_dir')
        self.assertEqual(self.shell.current_directory.name, 'test_dir')

if __name__ == '__main__':
    unittest.main()
