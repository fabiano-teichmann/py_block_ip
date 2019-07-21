from unittest import TestCase

from py_block_ip.read_file_rules import read_file


class TestLoadRules(TestCase):
    def test_load_paths(self):
        """Must be load file and return list"""
        paths = read_file('/home/fabiano/PycharmProjects/py_blocks_ip/py_block_ip/block.txt')
        self.assertIsInstance(paths, list)

    def test_path_not_exit(self):
        """Must be return msg error if path not exist"""
        paths = read_file('/home/fabiano/PycharmProjects/py_blocks_ip/py_block_ip/blockd.txt')
        self.assertIsInstance(paths, str)
        self.assertEqual(paths, 'Not found file')

    def test_file_invalid(self):
        """Must be retutn msg if path is invalid"""
        paths = read_file('/home/fabiano/PycharmProjects/py_blocks_ip/py_block_ip/file_invalid.txt')
        self.assertEqual(paths, 'file invalid de paths separated by line break, not for , or ;')
