import os
from unittest import TestCase
from faker import Faker

from py_block_ip.__main__ import protect_attack


class TestBlockIp(TestCase):
    def setUp(self):
        fake = Faker()
        self.ip = fake.ipv4()
        self.path = '/db/phpmyadmin/index.php'
        self.file = os.path.join(os.getcwd(), 'block.txt')

    def test_block_ip(self):
        msg = 'Must be return true'
        self.assertEqual(True, protect_attack(ip=self.ip, path=self.path, file_rules=self.file), msg=msg)

    def test_block_range_ip(self):
        resp = protect_attack(ip=self.ip, path=self.path, subnet='0/24')
        self.assertEqual(True, resp, msg='Must be blocked range 0/24')


