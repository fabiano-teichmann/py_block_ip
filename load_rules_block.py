
def path_deny(path=None):
    if path is None:
        path = 'block.txt'

    file_ = open(path, 'r').read()
    data = file_.split('\n')
    return [item for item in data if '#' not in item and item != '']

