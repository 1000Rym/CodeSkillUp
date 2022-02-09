# Fancy Progressbar in Python

## TQDM
[TQDM](https://github.com/tqdm/tqdm) is a fast, extensible progress bar for Python and CLI.

### Install TQDM
Command to run
```shell
pip install tqdm
```

### How to use TQDM
1. Input iterable objects to tqdm constructor.
    ```python
    for i in tqdm(range(100)):
        time.sleep(.1)
    ```
1. Input total progress in constructor.
    ```python
    pbar = tqdm(total= 100)
    for _ in range(100):
        time.sleep(.1)
        pbar.update(1)
        
    pbar.close()
    ```
1. Use with `trange`
    ```python
    from tqdm import trange
    for i in trange(100):
        time.sleep(1)
    ```
    - Nested Progressbar
        ```python
        for i in trange(4, desc='1st loop'):
            for j in trange(5, desc='2nd loop'):
                for k in trange(50, desc='3rd loop', leave=False):
                    time.sleep(0.01)
        ```

1. Make custom prgressbar
    ```python
    pbar = tqdm(range(100), desc= bar_name ,bar_format='{desc}: {percentage:3.0f}% {bar} {n_fmt}/{total_fmt}', postfix=None)
    
    for current_progress in range(total):
        pbar.n = current_progress
        pbar.refresh()
        time.sleep(sleep_interval)
    
    pbar.close()
    ```

- Source Code: [test_tqdm.py](test_tqdm.py)
