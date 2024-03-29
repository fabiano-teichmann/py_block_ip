import os


def read_file(file_=None):
    file_ = file_ if file_[0] != ' ' else file_[1:]
    file_ = file_ if file_[-1] != ' ' else file_[:-1]
    if os.path.isfile(file_):
        file_ = open(file_, 'r')
        data = file_.read()
        if ';' in data or ',' in data:
            return 'file invalid de paths separated by line break, not for , or ;'
        data = data.split('\n')
        file_.close()
        return [item for item in data if '#' not in item and item != '']
    else:
        return 'Not found file'

