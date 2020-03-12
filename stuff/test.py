
import os
from mmap import mmap

if __name__ == "__main__":
    file_handle = os.open("/dev/uio0", os.O_RDWR|os.O_NONBLOCK)
    mem_access = mmap(file_handle, 4)

    mem_access[0] = 10
    mem_access[1] = 00
    mem_access[2] = 10
    mem_access[3] = 00

    os.close(file_handle)
