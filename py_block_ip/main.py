from datetime import datetime

from decouple import config

from py_block_ip.block_access import ControlIptables
from py_block_ip.read_file_rules import read_file


def protect_attack(ip, path, subnet=False):
    """

    Args:
        ip (str):
        path (str): path url try access
        file_rules (str): path file content paths deny access if not passed file is used file default
        ip_accept (list): List ip accept
        subnet (str):  Use for blocked range ip
        will be blocked

    Returns:

    """
    paths_deny = config('pyblock_paths_deny', default='')
    ip_accept = config('pyblock_ip_accept', default='http://127.0.0.1')

    if ip in ip_accept:
        return False
    else:
        check_path = lambda x, y: True if x in y else False
        is_path_deny = [check_path(p, path) for p in paths_deny]

        if is_path_deny.count(True) > 0:
            if ControlIptables().lock_ip(ip, subnet):
                now = datetime.now()
                resp = f"Ip {ip} blocked try access path {path} - {now.strftime('%m/%d/%Y %H:%M:%S')} \n"
                file_log = config('PYBLOCK_LOGS', default='/var/log/pyblock_logs.logs')
                file_ = open(file_log, 'a')
                file_.write(resp)
                file_.close()
                print(resp)
        else:
            return False


def ip_is_allowed(ip, file_ip_accept=None):
    """
    Verify if ip is allowed
    Args:
        ip (str): ip
        file_ip_accept (str): path file content ip allowed

    Returns:
        bool
    """
    if file_ip_accept is not None:
        ip_accept = read_file(file_ip_accept)
        if ip in ip_accept:
            return True
        else:
            return False
    else:
        return False
