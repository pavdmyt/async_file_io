# -*- coding: utf-8 -*-

"""
sync_write
~~~~~~~~~~

Common synchronous files creation.
"""

import os
import shutil
import sys
import time

from constants import FILES_DIR


def create_file(fname, contents=""):
    with open(fname, 'w') as f:
        f.write(contents)


def main():
    try:
        qty = sys.argv[1]
    except IndexError:
        print("Error: no QTY specified")
        sys.exit(1)

    # Cleanup
    if os.path.exists(FILES_DIR):
        shutil.rmtree(FILES_DIR)
    os.mkdir(FILES_DIR)

    for i in range(1, int(qty) + 1):
        fname = "file_{}.txt".format(i)
        fpath = os.path.join(FILES_DIR, fname)
        create_file(fpath, "{}\n".format(i))


if __name__ == '__main__':
    start = time.time()
    main()
    print("__Passed: {}".format(time.time() - start))
