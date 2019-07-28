import configparser
import os

from py_block_ip.read_file_rules import read_file


def create_file_settings(ip_accept, paths_deny, log):
    """

    Args:
        ip_accept (str): path file content list accept. Ips has be separate for line break
        paths_deny (str): path file content list paths deny. Paths has be separate for line break
        log (str): path file where is save logs. If not pass path logs is saved in /var/log/pyblock_logs.log


    Returns:
        (str) return msg success or msg error
    """
    config = configparser.ConfigParser()
    config['settings'] = {}
    path = os.path.split(os.path.realpath(__file__))[0]
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

    with open(os.path.join(path, 'settings.ini'), 'w') as configfile:
        config.write(configfile)
    return "Configured with success."
