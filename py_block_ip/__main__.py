import argparse
from py_block_ip.main import protect_attack
from py_block_ip.settings import create_file_settings

parser = argparse.ArgumentParser(description='#### Py Block IP ####')
# Args for config
parser.add_argument('--config', dest="config", action="store_true",
                    help='Configure file content paths deny access and configure list ip with access')
parser.add_argument('--ip_accept', dest='ip_accept', type=str, help='Path file content ip not blocked')
parser.add_argument('--paths_deny', dest='paths_deny', type=str, help='Path file content paths for blocked deny')
parser.add_argument('--log', dest='log', type=str, help='Path file log')
# Args for run pyblock
parser.add_argument('--ip', dest="ip", type=str, help='ip requesting')
parser.add_argument('--path', dest="path", type=str,
                    help='path request')

parser.add_argument('--subnet', dest="subnet", type=str,
                    help='Use for deny range ip by default only ip request is blocked')


if __name__ == "__main__":
    args = parser.parse_args()
    if args.config:
        print(create_file_settings(args.ip_accept, args.paths_deny, args.log))
    elif args.ip and args.path:
        if args.subnet is None:
            protect_attack(ip=args.ip, path=args.path)
        else:
            protect_attack(ip=args.ip, path=args.path, subnet=args.subnet)

    else:
        print('Is necessary pass parameters ip and path')
