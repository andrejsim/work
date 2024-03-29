
import time
import multiprocessing 

def func(x):
    # code
    pass

def multiprocessing_func(x):
    time.sleep(1)
    print('{} {} number'.format(x, func(y)))
    
if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(0,100):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
        
    print('That took {} seconds'.format(time.time() - starttime))
