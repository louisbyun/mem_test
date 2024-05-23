import time
import numpy as np

def memory_write_speed_test(size_in_mb):
    data = np.random.bytes(size_in_mb * 1024 * 1024)
    start_time = time.time()
    memory_block = bytearray(data)
    end_time = time.time()
    write_speed = size_in_mb / (end_time - start_time)
    return write_speed

def memory_read_speed_test(memory_block):
    start_time = time.time()
    _ = memory_block[:]
    end_time = time.time()
    read_speed = len(memory_block) / 1024 / 1024 / (end_time - start_time)
    return read_speed

if __name__ == "__main__":
    size_in_mb = 100  # Memory size to test (MB)
    
    # Memory write speed test
    write_speed = memory_write_speed_test(size_in_mb)
    print(f"Memory Write Speed: {write_speed:.2f} MB/s")
    
    # Memory read speed test
    memory_block = bytearray(np.random.bytes(size_in_mb * 1024 * 1024))
    read_speed = memory_read_speed_test(memory_block)
    print(f"Memory Read Speed: {read_speed:.2f} MB/s")
