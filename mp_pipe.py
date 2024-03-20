## Pipe()클래스: multiprocessing.Pipe().
## 데이터를 공유하는 객체
## 메모리(RAM)를 기반으로 데이터 공유.
##Pipe()는 객체공유를 메모리를 기반으로 하기 때문에 사용가능한
##시스템 메모리의 한계에 따라 제한될 수 있다. 즉, 
#시스템의 물리적 메모리인 RAM이 부족하면 파이프를 통해 전달되는
#데이터 용량에 제한을 받을 수 있다.

#참고: 대용량 데이터 공유를 위해서는 Queue()나 Manager()를 이용!

import multiprocessing

def pro1(sender):
    sender.send('1234') #send()메서드에 보내는 데이터는 반복가능한 객체
    print("p1이 데이터를 보냈습니다.")

def pro2(receiver):
    item = receiver.recv() #데이터를 받는 메서드
    print(f"p2가 item {item}를 받아왔습니다.")

if __name__=='__main__':
    ps, pr = multiprocessing.Pipe() #두 개의 컨넥션 객체가 반환됨.(sender, receiver)

    p1 = multiprocessing.Process(target=pro1, args=(ps,))
    p2 = multiprocessing.Process(target=pro2, args=(pr,))
    
    p1.start()
    p2.start()
    print(multiprocessing.current_process())
    print(f"current process name:{multiprocessing.current_process().name} ")
    print(f"current process ID: {multiprocessing.current_process().pid}")
    
    ## 실행 중인 자식프로세스 리스트 출력
    active_processes = multiprocessing.active_children()
    print("Active Processes:")
    for process in active_processes:
        print(f"Name: {process.name}, ID:{process.pid}")
    p1.join()
    p2.join()
