# This python file is made for 
# the testing tqpm progress bar
from tqdm import tqdm, trange
import time

def test_tqdm(max_num, sleep_interval):
    """
    using tqdm module to render the progress bar.
    """
    for i in tqdm(range(max_num)):
        time.sleep(sleep_interval)
        
def test_tqdm_mannual(total, update_interval, sleep_interval):
    """
    using tqdm module with manual way.
    """
    pbar = tqdm(total= total)
    for _ in range(total):
        time.sleep(sleep_interval)
        pbar.update(update_interval)
        
    pbar.close()

        
def test_trange(max_num, sleep_interval):
    """
    using trange to renderering progress bar.
    """
    for i in trange(max_num):
        time.sleep(sleep_interval)


def test_nested_progressbar():
    """
    make a neseted progress bar.
    """
    for i in trange(4, desc='1st loop'):
        for j in trange(5, desc='2nd loop'):
            for k in trange(50, desc='3rd loop', leave=False):
                time.sleep(0.01)
    

def test_custom_progress_bar(total, bar_name, sleep_interval):
    pbar = tqdm(range(100), desc= bar_name ,bar_format='{desc}: {percentage:3.0f}% {bar} {n_fmt}/{total_fmt}', postfix=None)
    
    for current_progress in range(total):
        pbar.n = current_progress
        pbar.refresh()
        time.sleep(sleep_interval)
    
    pbar.close()
    

if __name__ == '__main__':
    test_tqdm(10, 0.1)
    test_trange(10, 0.2)
    test_tqdm_mannual(100, 10, 0.3)
    test_nested_progressbar()
    test_custom_progress_bar(100, 'first', .1)
    test_custom_progress_bar(100, 'second', .1)
    