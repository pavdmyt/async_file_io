# -*- coding: utf-8 -*-

"""
curio_async_read
~~~~~~~~~~~~~~~~

Asynchronous files reading with Curio:
https://github.com/dabeaz/curio
"""

import os
import time

import curio
from curio.file import aopen

from constants import FILES_DIR


async def read_file(fname):
    async with aopen(fname, 'r') as f:
        data = await f.read()
    return data


async def main():
    files_list = os.listdir(FILES_DIR)

    for fname in files_list:
        fpath = os.path.join(FILES_DIR, fname)
        await read_file(fpath)


if __name__ == '__main__':
    start = time.time()
    curio.run(main)
    print("__Passed: {}".format(time.time() - start))
