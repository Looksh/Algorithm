dice = list(map(int, input().split()))
dice.sort()
price = 0

if dice[0] == dice[1] == dice[2]:
    price = 10000 + (max(dice) * 1000)
elif dice[0] != dice[1] != dice[2]:
    price = max(dice) * 100
elif (dice[0] == dice[1]) or (dice[1] == dice[2]):
    price = 1000 + (dice[1] * 100)

print(price)
