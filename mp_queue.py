##프로세스 간의 객체 공유: Queue() 클래스 - put(), get()
##p1에서 데이터를 입력하고, p2에서 데이터를 읽어와서 출력하는 프로그램

from multiprocessing import Queue, Process
import time

def pro1(q):
    print(f"pro1: 1부터 99까지의 숫자를 리스트에 추가합니다.")
    #q에 데이터를 넣는다.
    for i in range(10):
        q.put(i)    ##put(): 데이터 입력하는 메서드
        time.sleep(1)

def pro2(q):
    items = []      ## get()한 데이터를 저장할 리스트
    while True:
        item = q.get()  ## q에 있는 데이터를 가지고 옮
        items.append(item)
        print(f"p2:q객체에서 {item}를 가져왔습니다.")
        print(f"현재 q에 저장된 값은 {items}입니다.")
        if len(items) == 10:
            break

## 메인코드 부분
if __name__ == "__main__":
    queue = Queue()     ##Queue 클래스의 객체 생성 후 queue 참조변수에 저장
    p1 = Process(target=pro1, args=(queue,))
    p2 = Process(target=pro2, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    p1.terminate()
    p2.terminate()