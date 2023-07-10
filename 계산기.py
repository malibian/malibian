
def 계산기(a,b):

    a = int(input("숫자를 입력하시오"))
    b = int(input("숫자를 입력하시오"))
    c = input("원하는 연산을 쓰세요")
    if c == "더하기":
        print(a+b)
    elif c == "빼기":
        print(a-b)
    elif c == "나누기":
        print(a%b)
    elif c == "곱하기":
        print(a*b)
        
    return c


