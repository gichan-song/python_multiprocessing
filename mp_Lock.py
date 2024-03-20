##Value객체 + Lock객체
##Lock객체: acquire(), release()
##Value('i', 0) --> v.value

import multiprocessing as mp
import time

def pro1(vl, lc):
    lc.acquire()    ## 락을 획득
    while vl.value < 10:
        print(f"현재 값은 {vl.value}")
        vl.value += 1
        time.sleep(1)
    lc.release()

def pro2(vl, lc):
    lc.acquire()
    while vl.value > -10:
        print(f"현재 값은 {vl.value}")
        vl.value -= 1
        time.sleep(1)
    lc.release()

if __name__ == "__main__":
    value = mp.Value('i', 0)
    lock = mp.Lock()
    p1 = mp.Process(target=pro1, args=(value, lock))
    p2 = mp.Process(target=pro2, args=(value, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()