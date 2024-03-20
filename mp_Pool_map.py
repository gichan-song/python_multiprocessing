## Pool(): 데이터를 여러프로세스가 병렬처리하기 위해 풀을 생성
## 즉, 반복가능 객체의 데이터를 여러프로세스가 나누어 실행.
## 주의: 함수 형태로만 사용 가능. 
## Pool 클래스의 주요기능:
## 1) 병렬처리 : cpu의 다중코어를 이용해서 병렬로 빠르게 처리.
## 2) 작업 스케쥴링: 내부적으로 작업을 자동으로 스케쥴링 --> 작업분배
## 3) 결과 수집: 각 프로세스에서 실행 결과 값을 AsyncResult객체로 반환. 
##  이 객체를 통해서 결과 값을 가져올 수 있음.
## 4) 자원관리: 생성된 프로세스들을 관리하고 작업이 완료되면 
##    자원을 정리해서 메모리 누수를 방지.

## 참고: 일반적으로 cpu집약적인 작업(예:계산)을 병렬로 처리하는데 
##      multiprocessing.Pool로 처리하면 성능을 향상 시킬 수 있음.
## map()메소드 : 반복 가능한 객체의 병렬처리

#############################################################
from multiprocessing import Pool
import multiprocessing

# Pool클래스는 함수형태로만 사용가능.
# map(f,[]) : f는 실행할 함수 이름. [](반복가능한 객체): 문자열, 리스트,
#            튜플, 딕셔너리 등... 

def f(x):
    return x * x


if __name__ == "__main__":
    pool = Pool() ##풀 객체를 생성 --> 
    #사용가능한 프로세스수와 동일한 수의 작업자 프로세스를 생성
    results = pool.map(f, [1, 2, 3]) 

    #부모프로세스 정보 출력
    print(f"Current process name: {multiprocessing.current_process().name}")
    print(f"Current process ID: {multiprocessing.current_process().pid}")

    #실행 중인 모든 자식 프로세스 리스트 출력
    active_processes = multiprocessing.active_children()
    print(f"{type(active_processes)}")
    print("Active Processes:")
    for process in active_processes:
       print(f"Name: {process.name}, ID: {process.pid}")

    pool.close() ## 더 이상 새로운 작업이 들어오지 못하도록 풀을 닫음.
    pool.join()  ## close()와 join()를 사용하여 프로세스 풀을 제대로
    # 종료해야 무한 루프에 빠지지 않음.
    print("풀이 정상적으로 종료되었습니다.")
    print("함수를 병렬처리한 결과:", results)



