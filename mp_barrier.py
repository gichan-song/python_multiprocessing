# ## Barrier() : 프로세스 간 동기화.
# ## multiprocessing.Barrier() 
# ## 베리어 개수를 제한하여 개수만큼 wait()하는 프로세스의 갯수가 채워지면
# ## 그 이후에 실행 가능.

# import multiprocessing
# import time

# def pro1(br, pn):
#     br.wait()
#     print(f"{pn}: process 1")

# def pro2(br, pn):
#     br.wait()
#     print(f"{pn}: process 2")

# if __name__ == "__main__":
#     barrier = multiprocessing.Barrier(2) #wait()하는 프로세스의 개수
#     p1 = multiprocessing.Process(target=pro1, args=(barrier, 'p1'))
#     p2 = multiprocessing.Process(target=pro2, args=(barrier, 'p2'))

#     p1.start()
#     time.sleep(2)
#     p2.start()
#     p1.join()
#     p2.join()

#########################################################
import multiprocessing

def worker_process(barrier, name):
    # Barrier를 사용하여 프로세스를 동기화하는 작업을 정의합니다.
    print(f'{name} started')
    barrier.wait()
    # 모든 프로세스가 Barrier에 도달할 때까지 대기합니다.
    print(f'{name} completed')

if __name__ == '__main__':
    # Barrier 객체 생성
    num_processes = 4  # 프로세스의 수
    barrier = multiprocessing.Barrier(num_processes) 
    ##프로세스가 4개가 wait()할 때 비로소 기능이 실행됨.

    # 프로세스 생성 및 시작
    processes = []
    for i in range(num_processes):  ##프로세스 4개를 생성한 후 
        process = multiprocessing.Process(target=worker_process, args=(barrier, f'Process {i}'))
        processes.append(process)
        process.start()

    # 프로세스 종료 대기
    for process in processes:
        process.join()

    print('All processes completed')
