# This program is illustrating
# multi-thread handling by using lock
import threading
import time

def func_for_thread1(numbers,lock):
    """
    Append number 11~20 to the input list
    """
    lock.acquire()
    for number in range(11, 21):
        time.sleep(0.1)
        numbers.append(number)
    lock.release()
    
def func_for_thread2(numbers, lock):
    """
    Append number 21~30 to the input list
    """
    lock.acquire()
    for number in range(21, 31):
        time.sleep(0.1)
        numbers.append(number)
    lock.release()
        
def func_for_thread3(numbers, lock):
    """
    Append number 31~40 to the input list
    """
    lock.acquire()
    for number in range(31, 41):
        time.sleep(0.1)
        numbers.append(number)
    lock.release()
    
def main():
    numbers = []
    
    lock = threading.Lock()
    
    t1 = threading.Thread(target=func_for_thread1, args=(numbers, lock,))
    t2 = threading.Thread(target=func_for_thread2, args=(numbers, lock,))
    t3 = threading.Thread(target=func_for_thread3, args=(numbers, lock,))
    
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    count = 0
    for number in numbers:
        count +=1
        print(number, end=" ")
        if count % 10 == 0: 
            print()
    
if __name__ == '__main__':
    main()
    
        
