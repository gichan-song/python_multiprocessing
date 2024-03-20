## two ways to start process
## 1.spawn, 2.fork
## 1) spawn : create process from code // windows systems are only possible this way. of course linux, macOS systems can use this way
## 2) fork : copy parent process. it goes fast to create process.
##           But because of many of codes and data, it can cause system overload. // linux, macOs

# import multiprocessing

# def start_process():
#     return 1

# ## maincode section
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=start_process)
#     p1.start()

#     print(multiprocessing.get_start_method())   ##spawn
#     ## currently being used os is windows, process method is spawn
#     ## linux : base is fork, to use spawn: multiprocessing.set_start_method("spawn")
#     p1.join()
#     p1.terminate()

#################################################################################################
## start with creating several processes

import multiprocessing as mp    ##as alias

def worker_process(name):
    ## define process work
    print(f"Worker process {name} started")
    ## print that process has started

if __name__ == "__main__":
    num_processes = 4 # set number of processes to create
    # process list
    processes = []

    ## create and start multiprocess
    for i in range(num_processes):
        p = mp.Process(target=worker_process, args=(i,))
        p.start()
        processes.append(p)
    
    for i in processes:
        i.join()
        i.terminate()

    print("All processes completed")