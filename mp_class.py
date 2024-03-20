from multiprocessing import Process, freeze_support
##클래스로 선언하는 방법
# class HelloProcess(Process):
#     def __init__(self):
#         super(Process, self).__init__() ##슈퍼클래스의 생성자 호출

#     def run(self):  ##run()메서드: 자동 수행
#         print("Hello Process2")

# ##메인코드 부분
# if __name__ == "__main__":
#     freeze_support()
#     p1 = HelloProcess()
#     p1.start()
#     p1.join()
#     p1.terminate()
##########################################################################
# 클래스선언 부분
class HelloProcess(Process):
    def __init__(self, arg1, arg2):
        super(Process, self).__init__()

    def run(self):
        print("Hello Process2")

## 메인코드 부분
if __main__ == "__main__":
    freeze_support()
    p1 = HelloProcess(1, arg2="Hello")
    p1.start()
    p1.join()
    p1.terminate()