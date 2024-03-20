#Event()클래스: 프로세스 동기화. 프로세스를 동시에 실행하도록...
#여러 프로세스가 어떤 신호에 의해서 실행되도록 함.
# ex) sleep()메소드를 이용해서 3초 뒤 두 개의 프로세스가 동시에 실행되도록 할 수 있다.

# import multiprocessing
# import time

# def pro1(evt):
#     evt.wait() #이벤트객체가 설정(set)되기를 기다림
#     # 이벤트 객체가 설정되면 
#     # evt.wait()는 반환된 후 이후코드가 실행됨. 
#     # set()메서드를 호출하지 않으면 evt.wait()가 
#     # 블로킹되어 프로세스가 대기 상태로 들어감.
#     print(f"p1프로세스 입니다.")

# def pro2(evt):
#     evt.wait()
#     print(f"p2프로세스 입니다.")


# if __name__ == "__main__":

#     event = multiprocessing.Event()  #이벤트 객체 생성
#     p1 = multiprocessing.Process(target=pro1, args=(event,))
#     p2 = multiprocessing.Process(target=pro2, args=(event,))
#     p1.start()
#     p2.start()
#     time.sleep(3)
#     event.set() #event객체가 설정(set())되도록 호출
#     p1.join()
#     p2.join()

