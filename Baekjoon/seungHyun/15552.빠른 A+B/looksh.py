import sys
for i in range(int(input())):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)

[시간을 최대한 줄이도록 노력]
=> t = int(input) 라인을 제거
map 함수와 sys,stdin,readline 이용 입출력 속도 개선
