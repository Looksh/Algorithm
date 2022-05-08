[풀이]
- 시간, 분 구하는 공식을 알아야한다
- timer 의 시간, 분을 구하고 더한 후 조건문을 붙힌다  

hour, minute = map(int, input().split())
timer = int(input())

hour += timer // 60
minute += timer % 60

if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24

print(f'{hour} {minute}')
