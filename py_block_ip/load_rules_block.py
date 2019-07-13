
def read_file(file_=None):
    path = file_
    file_ = open(path, 'r')
    data = file_.read()
    data = data.split('\n')
    file_.close()
    return [item for item in data if '#' not in item and item != '']

