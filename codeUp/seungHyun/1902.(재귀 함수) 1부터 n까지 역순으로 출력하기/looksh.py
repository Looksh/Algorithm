n = int(input())

def seq(n):
    print(n)
    if n == 1:
        return
    else:
        n -= 1
        seq(n)

seq(n)
