# This program is made for illustrating the single thread concept.
import threading
import time

def print_cube(num):
    """
    print cube of the given num
    """
    print(f"Cube of {num} is {num*num*num}")
    print(f"Thread id:{threading.current_thread().ident}, name: {threading.current_thread().name}")

def print_msg_after_n_seconds(n):
    """
    print the message after n seconds
    """
    time.sleep(n)
    print(f"The message printed after {n} seconds")
    
def print_squre(num):
    """
    print the square of the given num
    """
    print(f"Squre of {num} is {num*num}")
    print(f"Thread id:{threading.current_thread().ident}, name: {threading.current_thread().name}")

def main():
    print(f"Main Thread name:{threading.current_thread().name}, id: {threading.get_ident()}")
    
    t1 = threading.Thread(target=print_cube, args=(10,), name='t1_cube_thread')
    t2 = threading.Thread(target=print_squre, args=(10,), name='t2_print_squre')
    t3 = threading.Thread(target=print_msg_after_n_seconds, args=(10,), name='t3_msg')
    
    # start the thread1 and thread2.
    t1.start()
    t2.start()
    t3.start()
    
    msg =input("Please input any message:")
    print("msg:", msg)
    
    # Wait for the thread t1 and t2 is completely finished.
    t1.join()
    t2.join()
    t3.join()
    
    print("Finish program")    

if __name__  == '__main__':
    main()