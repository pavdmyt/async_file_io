# -*- coding: utf-8 -*-

"""
sync_read
~~~~~~~~~

Synchronous files reading.
"""

import os
import time

from constants import FILES_DIR


def read_file(fname):
    with open(fname, 'r') as f:
        data = f.read()
    return data


def main():
    files_list = os.listdir(FILES_DIR)

    for fname in files_list:
        fpath = os.path.join(FILES_DIR, fname)
        read_file(fpath)


if __name__ == '__main__':
    start = time.time()
    main()
    print("__Passed: {}".format(time.time() - start))
