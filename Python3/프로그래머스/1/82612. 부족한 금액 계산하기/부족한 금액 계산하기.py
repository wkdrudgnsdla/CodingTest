def solution(price, money, count):
    answer = -1
    before_price = price
    for i in range(count + 1):
        money -= price * i
        print(money)
    if money < 0:
        answer = money * -1
    else:
        answer = 0
    return answer