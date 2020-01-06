import os
import subprocess as sb


# This Simple code that arranges a Directory in a Sub-directories with all same type files in sorted format.
# INPUT: A valid dir path to be arranged.

def sorter(path):
    try:
        os.chdir(path)
        files = sb.getoutput("ls").split('\n')

        for file in files:
            if '.' in file and not os.path.isdir(path + '/' + file):
                dir_name = file[file.rindex(".") + 1:].lower()

                if not is_listed(path, dir_name):
                    
                    os.mkdir(path + '/' + dir_name)
                    new_path = path + '/' + dir_name + '/' + file
                    relocate(path + '/' + file, new_path)

                else:
                    
                    new_path = path + '/' + dir_name + '/' + file
                    relocate(path + '/' + file, new_path)

            elif not is_dir(path, file):
                
                if not is_listed(path, "etc_files"):
                    
                    os.mkdir(path + '/' + "etc_files")

                if is_listed(path, "etc_files"):
                    
                    new_path = path + '/' + "etc_files" + '/' + file
                    relocate(path + '/' + file, new_path)

        return "[+] Successfully sorted all files"

    except Exception as e:
        return e


def is_listed(path, target):
    files = os.listdir(path)
    for f in files:
        if target == f:
            return True
    return False


def is_dir(path, file):
    if os.path.isdir(path + '/' + file):
        return True
    else:
        return False


def relocate(path, new_path):
    os.rename(path, new_path)


if __name__ == "__main__":
    dir_path = input("Input path: ")
    print(sorter(dir_path))
