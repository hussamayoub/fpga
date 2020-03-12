
import os 
from mmap import mmap

if __name__ == "__main__":

	file_handle = os.open("/dev/uio1", os.O_RDWR | os.O_NONBLOCK)
	mem = mmap(file_handle,16)
	temparr = mem[12:14]
	while 1:
		na = int.from_bytes(mem[12:14], byteorder='little' , signed=True)
		print(na)
	os.close(file_handle)

