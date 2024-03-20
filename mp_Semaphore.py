import multiprocessing as mp
import time

# def pro1(sm, pn):
#     sm.acquire()
#     print(f"pro1: {pn}프로세스가 세마포어를 획득했습니다.")
#     print(f"세마포어가 실행중...")
#     sm.release()
#     print(f"세마포어가 릴리즈 됩니다.")

# def pro2(sm, pn):
#     sm.acquire()
#     print(f"pro2: {pn}프로세스가 세마포어를 획득했습니다.")
#     print(f"pro2: {pn}프로세스 실행 중...")
#     print(f"{pn}프로세스가 릴리즈 됩니다.")
#     sm.release()

# if __name__ == "__main__":
#     sema = mp.Semaphore(1)
#     p1 = mp.Process(target=pro1, args=(sema, "p1"))
#     p2 = mp.Process(target=pro2, args=(sema, "p2"))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

def worker_process(sm, index):
    sm.acquire()
    print(f"worker_process {index}가 시작되었습니다.")
    time.sleep(1)
    print(f"프로세스 {index}가 종료되었습니다.")
    sm.release()
    print(f"프로세스 {index}: 세마포어를 릴리즈했습니다.")

if __name__ == "__main__":
    processes = []
    semaphore = mp.Semaphore(2)
    for i in range(4):
        process = mp.Process(target=worker_process, args=(semaphore, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("모든 프로세스가 완료되었습니다.")