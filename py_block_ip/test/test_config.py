from unittest import TestCase

from py_block_ip.main import create_file_settings
from py_block_ip.read_file_rules import read_file


class TestConfig(TestCase):

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

    def test_create_file_settings(self):
        """Must be create file settings.ini"""
        paths_deny = '/home/fabiano/PycharmProjects/py_blocks_ip/py_block_ip/block.txt'
        ip_accept = '/home/fabiano/PycharmProjects/py_blocks_ip/py_block_ip/ip_accept.txt'
        self.assertEqual(create_file_settings(ip_accept, paths_deny), 'Configured with success.')

