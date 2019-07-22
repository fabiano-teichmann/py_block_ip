import argparse

from py_block_ip.main import protect_attack
from py_block_ip.settings import create_file_settings

parser = argparse.ArgumentParser(description='#### Py Block IP ####')
parser.add_argument('--config', dest="config", action="store_true",
                    help='Configure file content paths deny access and configure list ip with access')
parser.add_argument('--ip', dest="ip", type=str,
                    help='ip requesting')
parser.add_argument('--path', dest="path", type=str,
                    help='path request')

parser.add_argument('--subnet', dest="subnet", type=str,
                    help='Use for deny range ip by default only ip request is blocked')


if __name__ == "__main__":
    args = parser.parse_args()
    if args.config:
        paths_deny = input('Insert path file content paths for protect (required) ')
        ip_accept = input('Insert path file content ip with acess allowed (not required) ')
        log = input('Insert path file log (not required) ')
        print(create_file_settings(ip_accept, paths_deny, log))
    elif args.ip and args.path:
        if args.subnet is None:
            protect_attack(ip=args.ip, path=args.path)
        else:
            protect_attack(ip=args.ip, path=args.path, subnet=args.subnet)

    else:
        print('Is necessary pass parameters ip and path')
