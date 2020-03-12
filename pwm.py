
import os
from mmap import mmap

if __name__ == "__main__":
    file_handle = os.open("/dev/uio0", os.O_RDWR|os.O_NONBLOCK)
    mem_access = mmap(file_handle, 4)

    mem_access[0] = 129
    mem_access[1] = 129
    mem_access[2] = 129
    mem_access[3] = 129

    os.close(file_handle)
