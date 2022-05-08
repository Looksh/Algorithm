n = int(input())
rec = n-(n-1)

def seq(rec):
    if rec == n:
        print(n)
        return
    else:
        print(rec)
        rec += 1
    seq(rec)

seq(rec)
