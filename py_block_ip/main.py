import argparse
import configparser
from py_block_ip.block_access import ControlIptables
from py_block_ip.read_file_rules import read_file

parser = argparse.ArgumentParser(description='#### Py Block IP ####')
parser.add_argument('--config', dest="config", action="store_true",
                    help='Configure file content paths deny access and configure list ip with access')
parser.add_argument('--ip', dest="protect", type=str,
                    help='ip requesting')
parser.add_argument('--path', dest="protect", type=str,
                    help='path request')

parser.add_argument('--subnet', dest="protect", type=str,
                    help='Use for deny range ip by default only ip request is blocked')


def protect_attack(ip, path, file_rules=None, ip_accept=None, subnet=False):
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
    try:
        paths_deny = read_file(file_rules)
    except Exception as e:
        raise e
    if ip_accept is not None:
        if ip in ip_accept:
            return False
        else:
            check_path = lambda x, y: True if x in y else False
            is_path_deny = [check_path(p, path) for p in paths_deny]

            if is_path_deny.count(True) > 0:
                return ControlIptables().lock_ip(ip, subnet)
            else:
                return False
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


def create_file_settings():
    config = configparser.ConfigParser()
    ip_accept = input('Insert path file content ip with acess allowed')
    paths_deny = input('Insert path file content paths for protect')
    rules = read_file(paths_deny)
    ips = read_file(ip_accept)
    config['settings'] = {}
    config['settings']['PYBLOCK_IP_ACCEPT'] = ", ".join(x for x in ips)
    config['settings']['PYBLOCK_PATHS_DENY'] = ", ".join(x for x in rules)
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.config:
        pass
    elif args.ip and args.path:
        protect_attack(ip=args.ip, path=args.path, subnet=args.subnet)
    else:
        print('Is necessary pass parameters ip and path')
