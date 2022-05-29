import os
import threading
from tqdm import tqdm
import time

MAX_THREAD = 5
TIME_INTERVAL = 1

        
def copy_file(desc, src, dst):
    """ Copy file from source to destination
    Args:
        src (string): The path of source file.
        dst (string): The path of destination file.
    """
    
    # Change to MB
    mb_size = 1024**2
    fsize = int(os.path.getsize(src))//mb_size

    
    with open(src, 'rb') as fsrc:
        with open(dst, 'ab') as fdst:
            with tqdm(ncols = 60, total = fsize, bar_format = '{l_bar}{bar} | Speed: {rate_fmt}', unit = "MB", desc= desc) as pbar:
                buffer = bytearray()
                curr_size = 0   
                while True:
                    buf = fsrc.read(8192)
                    fdst.write(buf)  
                    curr_size += len(buf)
                    
                    if curr_size >= mb_size:
                        pbar.update(curr_size//mb_size)
                        curr_size=0
                        
                    if len(buf) == 0:
                        break
                            
            
def main():
    src = "/Users/cheonlim/Desktop/test1.mp4"
    dst_folder = "/Users/cheonlim/Desktop/"
    thread_list = []
    
    for i in range(MAX_THREAD):
        name = "test " + str(i+1)
        dst = dst_folder + name
        thread_list.append(threading.Thread(target = copy_file, args=(name,src,dst), name=name))
        
    
    for thread in thread_list:
        thread.start()
        time.sleep(TIME_INTERVAL)
        
if __name__ == '__main__':
    main()