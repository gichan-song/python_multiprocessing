from multiprocessing import SimpleQueue, Process
import time

def pro1(sq):
    for i in range(10):
        sq.put(i)
        print(f"p1: SimpleQueue 객체에 {i}를 담았습니다.")
        time.sleep(0.5)

def pro2(sq):
    items = []
    while True:
        item = sq.get()
        if item is None:
            print(f"p2: SimpleQueue의 내용을 모두 가져왔습니다.")
            break
        print(f"p2:SimpleQueue의 값: {item}")
        items.append(item)
    print(f"p2: 리스트에 담은 값은 {items} 입니다.")


if __name__ == "__main__":

    sq = SimpleQueue()
    p1 = Process(target=pro1, args=(sq,))
    p2 = Process(target=pro2, args=(sq,))

    p1.start()
    p2.start()

    p1.join()
    sq.put(None)        ##get()메서드는 데이터가 들어올 때까지 대기상태에 있으므로
                        ##대기를 멈추게 하기 위해서 put()메서드를 통해서 None이라는 값을
                        ##SImpleQueue에 전달을 하고, p2에서는 값을 확인하는 작업을 통해서
                        ##데이터 입력의 끝의 여부를 확인
    p2.join()