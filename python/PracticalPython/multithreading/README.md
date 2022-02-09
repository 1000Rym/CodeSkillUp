# Multithreading in python
## Thread
### What is the thread?
- Entity within a process that can be scheduled for execution.
- __smallest unit of processing__ that can be performed in an OS(Operating System).
- Sequence of such instructions within a program that can be executed independently of other code.
- Think as the subset of a process.
### TCB(Thread Control Block)
- __Thread Identifier__: TID
- __Stack Pointer__: Contains the local variables under thread's scope.
- __Program counter__: A register which stores the address of the instuction currently being executed by thread.
- __Thread state__: State of the thread(running, ready, waiting, start, done).
- __Thread's register set__: register assinged to thread for comutations.
- __Parent process pointer__: A pointer to PCB of the process that the thread lives on.

### Thread Basic in Python
- Import and Declare Thread Object
    ```python
    import threading
    thread_var = threading.Thread(target=func_name, args=(iterable), name = 'thread_name')
    ```
- Start & Join Thread
    ```python
    thread_var.start()
    // current thread wait until the thread_var finished.
    thread_var.join() 
    ```
- Example Code: [single_thread_concept.py](single_thread_concept.py)

## Synchronization between threads
To avoid __critical section__. 
- Ensures that two or more concurrent threads do not simultaneously execute some particualr program segment known as critical section.

- How to? 
use the thread lock.
```python
lock = threading.Lock()

# from the thread
lock.acquire() 
# do some process
lock.release()
```

- Example Code: [multithreading_lock.py](multithreading_lock.py)

## Other Notes
In python any thread can make subthreads, and they were not managed in hierarchy.
reference: [Can threads create sub-threads in Python?](https://stackoverflow.com/questions/44908661/can-threads-create-sub-threads-in-python)

## Reference
- [Multithreading in Python](https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/?ref=rp)

