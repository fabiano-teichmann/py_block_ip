import configparser
from datetime import datetime

from decouple import config
from py_block_ip.read_file_rules import read_file
from py_block_ip.block_access import ControlIptables


def protect_attack(ip, path, subnet=False):
    """

    Args:
        ip (str):
        path (str): path url try access
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


def create_file_settings(ip_accept, paths_deny, log):
    config = configparser.ConfigParser()
    config['settings'] = {}

    rules = read_file(paths_deny)
    if isinstance(rules, list):
        config['settings']['PYBLOCK_PATHS_DENY'] = ", ".join(x for x in rules)
    else:
        return f"{rules} content paths for protect"
    if ip_accept:
        ips = read_file(ip_accept)
        if isinstance(ips, list):
            config['settings']['PYBLOCK_IP_ACCEPT'] = ", ".join(x for x in ips)
        else:
            return f"{ips} File ips"
    else:
        config['settings']['PYBLOCK_IP_ACCEPT'] = " "

    if log:
        config['settings']['PYBLOCK_LOGS'] = log
    else:
        config['settings']['PYBLOCK_LOGS'] = '/var/log/pyblock_logs.log'

    with open('settings.ini', 'w') as configfile:
        config.write(configfile)
    return "Configured with success."


