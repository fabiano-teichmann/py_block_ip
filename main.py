from load_rules_block import path_deny


def protect(func):
    def block(ip, path):
        paths_deny = path_deny()
        check_path = lambda x, y: True if x in y else False
        is_path_deny = [check_path(p, path) for p in paths_deny]
        if is_path_deny.count(True) > 0:
            func()
            block(ip)
        else:
            func()


