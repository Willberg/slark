import os


def mkdir_loop(base_path):
    if os.path.exists(base_path):
        return True

    dirs = base_path.split('/')
    dirs = dirs[:len(dirs) - 1] if dirs[len(dirs) - 1] == '' else dirs
    dirs = dirs[1:] if dirs[0] == '' else dirs

    # 循环创建目录
    d = ''
    for t in dirs:
        d += '/' + t
        if not os.path.exists(d):
            os.mkdir(d)

    return True
