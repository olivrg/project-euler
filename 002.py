def fibonacci_gen(n):  
    a, b = 1, 1
    while b <= n:
        a, b = b, a + b
        yield a

def solution(n):  
    return sum(i for i in fibonacci_gen(n) if not i % 2)

if __name__ == '__main__':  
    print(solution(4000000))
