## Pool클래스 apply(), apply_async()메소드:
## 1) apply() : 동기적 처리. 함수를 동기적으로 실행하여 결과를 반환.
##       순차적 실행 -- 블로킹        
## 2) apply_async() : 비동기적 처리
##    함수의 실행이 끝나기 전에 기다리지 않고 바로 다음작업을 실행 -블로킹x
##    각 프로세스는 할당된 작업을 비동기적으로 실행
## 주의: 위 두개의 메소드의 인자 값은 한 개여야 함.
## 즉, 리스트[], tuple 등의 반복 가능한 객체 속에 여러 개의 요소 값을 넘겨
## 줄 때 그 내부 요소의 갯수만큼 매개변수로 받아야 함.

from multiprocessing import Pool

def f(x1, x2, x3, a):  
    # x매개변수는 반복가능한 객체의 요소수와 동일하여야 함.
    print(f"a:{a}")
    return x1 * x2 * x3

if __name__ == '__main__':
    pool = Pool()  # 풀 생성
    print(pool.apply(f, [3, 4, 5], {'a':4}))
    
    ## apply_async()를 이용한 비동기 처리
    res = pool.apply_async(f, [1, 2, 3], {'a':5})
    print(f"비동기적 처리결과: {res}")
    print(res.get()) ##결과 값을 가져옴.
    pool.close()
    pool.join()   