import multiprocessing as mp
import time

### 조건을 기다리다가 실행하는 함수
### 3개의 프로세스를 동일한 컨디션 객체를 이용해서 기다리게 하고 깨우는 프로그램.
## p1, p2, p3 프로세스를 만들고 p3가 p1, p2를 깨우는 역할 담당.
## 메서드: acquire(), wait(), notify(), notify_all(), release()

def pro1(c, pn):
    print(f"{pn}가 컨디션 객체를 획득합니다.")
    c.acquire() ##컨디션 객체를 획득
    c.wait()    ##특정 조건이 될 때까지 기다림
    print(f"{pn}프로세스의 기다림이 끝났습니다. pro1 동작 중...")
    c.release() ##컨디션 객체를 반환

def pro2(c, pn):
    c.acquire() ##컨디션 객체를 획득
    # c.notify_all() ##모든 프로세스들을 깨우는 역할
    c.notify() ## 임의의 프로세스 하나를 깨우는 역할
    # c.notify()
    c.release()

if __name__ == "__main__":
    cond = mp.Condition()
    p1 = mp.Process(target=pro1, args=(cond, "p1"))
    p2 = mp.Process(target=pro1, args=(cond, "p2"))
    p3 = mp.Process(target=pro2, args=(cond, "p3"))

    p1.start()
    p2.start()
    time.sleep(3)
    p3.start()

    p1.join()
    p2.join()
    p3.join()

# def worker_process(condition, pn):
#     print(f"{pn}프로세스가 시작되었습니다.")
#     condition.acquire()
#     condition.wait()    ##notify를 기다리다가
#     print(f"{pn}프로세스가 완료되었습니다.")
#     condition.release()

# if __name__ == "__main__":
#     condition = mp.Condition()
#     process1 = mp.Process(target=worker_process, args=(condition, "p1"))
#     process2 = mp.Process(target=worker_process, args=(condition, "p2"))

#     process1.start()
#     process2.start()
#     time.sleep(3)
#     condition.acquire() ##컨디션객체 획득
#     # condition.notify_all() ##모든 프로세스 깨움
#     condition.notify()
#     condition.notify()
#     condition.release()

#     process1.join()
#     process2.join()

#     print("모든 프로세스가 끝이 났습니다.")