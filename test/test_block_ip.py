from unittest import TestCase


from main import protect_attack


class TestBlockIp(TestCase):
    def setUp(self):
        self.ip = '192.168.25.11'
        self.path = '/db/phpmyadmin/index.php'

    def test_block_ip(self):
        self.assertEqual(True, protect_attack(ip=self.ip, path=self.path), msg='Must be return true')
