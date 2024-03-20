##멀티프로세스를 함수로 정의
from multiprocessing import Process, freeze_support

#함수 정의
def Hello():
    print("Hello Process")

##메인코드 부분: 함수 호출
if __name__ == "__main__":
    freeze_support() ## call freeze_support() on Windows Systems when using multiprocessing

    p1 = Process(target=Hello)
    p1.start()      ## start process
    p1.join()       ## wait until terminate
    p1.terminate()