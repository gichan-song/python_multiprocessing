##  Manager클래스로 객체 공유하기
import multiprocessing as mp

def pro1(mn, pn):
    mn.append("p1")
    print(f"{pn}현재 리스트의 값: {mn}")

def pro2(mn, pn):
    mn.append("p2")
    print(f"{pn}현재 리스트에 값을 추가했습니다. {mn}")

if __name__ == "__main__":
    mn = mp.Manager()
    manager_list = mn.list()    ##빈 리스트 생성[]
    #manager_list = mn.dict()   ##빈 딕셔너리 생성{}
    p1 = mp.Process(target=pro1, args=(manager_list, "p1"))
    p2 = mp.Process(target=pro2, args=(manager_list, "p2"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()   