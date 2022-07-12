__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# importing os module
import os
import shutil
from os.path import abspath
from zipfile import ZipFile

# CWD

cwd = os.getcwd()


# Directory
directory = "cache"

# Parent Directory path
parent_dir = cwd

# Path
path = os.path.join(parent_dir, directory)


def clean_cache():

    if os.path.isdir(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        return

    else:
        os.mkdir(path)


def cache_zip(file_path, cache_dir_path):
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile(file_path, 'r') as zipObj:
       # Extract all the contents of zip file in different directory
        zipObj.extractall(cache_dir_path)


def cached_files():
    res = []
    for entry in os.scandir(path):
        if entry.is_file():
            res.append(os.path.abspath(entry))
    res.sort()
    return res


def find_password(files):
    string1 = 'password'

    for file in files:
        f = open(file, "r")
        str_list = f.readlines()

        for str in str_list:
            if string1 in str:
                return str.split("password: ")[1]


def main():

    clean_cache()

    zipfile_location = f"{cwd}/data.zip"
    cachefiles_location = f"{cwd}/cache"

    cache_zip(zipfile_location, cachefiles_location)

    files = cached_files()

    password = find_password(files)
    print(password)


if __name__ == '__main__':

    # calls here
    main()
