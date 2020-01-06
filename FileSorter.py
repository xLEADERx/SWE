import os
import subprocess as sb
from sys import platform as _platform

# This Simple code that arranges a Directory in a Sub-directories with all same type files in sorted format.
# INPUT: A valid dir path to be arranged.


def check_os():
    global sep
    if _platform == "linux" or _platform == "linux2":
        sep = '/'
        return 'ls'
    # linux
    elif _platform == "darwin":
        sep = '/'
        return 'ls'
    # MAC OS X
    elif _platform == "win32":
        sep = '\\'
        return 'dir /b'
    # Windows
    elif _platform == "win64":
        sep = '\\'
        return 'dir /b'


def sorter(path):
    try:
        os.chdir(path)
        files = sb.getoutput(check_os()).split('\n')

        for file in files:
            if '.' in file and not os.path.isdir(path + sep + file):
                dir_name = file[file.rindex(".") + 1:].lower()

                if not is_listed(path, dir_name):

                    os.mkdir(path + sep + dir_name)
                    new_path = path + sep + dir_name + sep + file
                    relocate(path + sep + file, new_path)

                else:

                    new_path = path + sep + dir_name + sep + file
                    relocate(path + sep + file, new_path)

            elif not is_dir(path, file):

                if not is_listed(path, "etc_files"):
                    os.mkdir(path + sep + "etc_files")

                if is_listed(path, "etc_files"):
                    new_path = path + sep + "etc_files" + sep + file
                    relocate(path + sep + file, new_path)

        return "[+] Successfully Sorted all files"

    except Exception as e:
        return e


def is_listed(path, target):
    files = os.listdir(path)
    for f in files:
        if target == f:
            return True
    return False


def is_dir(path, file):
    if os.path.isdir(path + sep + file):
        return True
    else:
        return False


def relocate(path, new_path):
    os.rename(path, new_path)


if __name__ == "__main__":
    sep = '/'
    dir_path = input("Input path: ")
    print(sorter(dir_path))
