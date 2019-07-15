from py_block_ip.block_access import ControlIptables
from py_block_ip.load_rules_block import read_file


def protect_attack(ip, path, file_rules=None, ip_accept=None):
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
                return ControlIptables().lock_ip(ip)
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

