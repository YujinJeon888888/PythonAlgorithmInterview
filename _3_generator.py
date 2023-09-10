def get_natural_number():
    n = 0
    while n < 100:
        n += 2
        yield n

gen = get_natural_number()  # 제너레이터 객체를 생성합니다.

for i in range(10):
    print(next(gen))  # next() 함수를 사용하여 제너레이터에서 값을 하나씩 가져옵니다.

##########################

#여러 타입을 yield 가능
def generator():
    yield 1
    yield 'string'
    yield True

g = generator()
print("여러 타입 yield 예제 ↓")
print(next(g))
print(next(g))
print(next(g))