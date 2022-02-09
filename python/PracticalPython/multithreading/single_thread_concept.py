# This program is made for illustrating the single thread concept.
import threading

def print_cube(num):
    """
    print cube of the given num
    """
    print(f"Cube of {num} is {num*num*num}")
    print(f"Thread id:{threading.current_thread().ident}, name: {threading.current_thread().name}")

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
    
    # start the thread1 and thread2.
    t1.start()
    t2.start()
    
    # Wait for the thread t1 and t2 is completely finished.
    t1.join()
    t2.join()
    
    print("Finish program")    

if __name__  == '__main__':
    main()