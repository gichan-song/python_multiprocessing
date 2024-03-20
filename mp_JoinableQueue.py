####JoinableQueue()클래스: 프로세스 간 데이터를 공유
## 카운터가 없으므로 작업의 종료를 알리는 task_done()이 필요함 

import multiprocessing
from time import sleep

def pro1(jq, pn):
    for i in range(10):
        jq.put(i)
        print(f"{pn}:jq에 값 {i}를 입력했습니다.")
        sleep(0.5)

def pro2(jq, pn):
    items = []
    while True:
        item = jq.get()
        if item is None:
            print(f"{pn}:모든 jq객체의 데이터를 가져왔습니다.")
            break
        items.append(item)
        print(f"{pn}:jq객체로 부터 {item}을 가져왔습니다.")
    print(items)
    jq.task_done()  
    ## JoinableQueue는 카운터가 없으므로 작업의 종료를 알려주어야 함.


if __name__ == '__main__': #메인코드 블럭이 실행되도록 보장
    jqueue = multiprocessing.JoinableQueue()
    p1 = multiprocessing.Process(target=pro1, args=(jqueue, "p1") )
    p2 = multiprocessing.Process(target=pro2, args=(jqueue, "p2") )

    p1.start()
    p2.start()

    p1.join() 
    jqueue.put(None)
    p2.join()