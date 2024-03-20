from multiprocessing import Process, Value, freeze_support
import time

def pro1(v, pn):
    print(f"Value 객체의 초기값: {v}")
    print(f"{pn} Value 객체의 초기값: {v.value}") #p1 Value 객체의 초기값: 0
    pro2(v,pn)

def pro2(v, pn):
    # time.sleep(3)
    v.value = 10
    print(f"{pn} pro2에서 입력된 값: {v.value}")

if __name__ == "__main__":
    value = Value('i', 0)
    ##데이터 공유를 위해 Value 객체를 생성. i는 정수를 의미, 초기값 0
    p1 = Process(target=pro1, args=(value,"p1"))
    p2 = Process(target=pro2, args=(value,"p2"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()