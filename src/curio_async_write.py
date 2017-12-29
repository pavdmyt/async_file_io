# -*- coding: utf-8 -*-

"""
curio_async_write
~~~~~~~~~~~~~~~~~

Asynchronous files creation with Curio:
https://github.com/dabeaz/curio
"""

import os
import shutil
import sys
import time

import curio
from curio.file import aopen

from constants import FILES_DIR


async def create_file(fname, contents=""):
    async with aopen(fname, 'w') as f:
        await f.write(contents)


async def main():
    try:
        qty = sys.argv[1]
    # XXX: does not fails gracefully
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
        await create_file(fpath, "{}\n".format(i))


if __name__ == '__main__':
    start = time.time()
    curio.run(main)
    print("__Passed: {}".format(time.time() - start))
