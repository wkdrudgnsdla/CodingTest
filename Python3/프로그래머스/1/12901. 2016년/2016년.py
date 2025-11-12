def solution(a, b):
    answer = ''
    day = 0
    month_days = [31,29,31,30,31,30,31,31,30,31,30,31]

    for i in range(1, a):
        day += month_days[i-1]

    day += b

    if day % 7 == 1:
        answer = "FRI"
    elif day % 7 == 2:
        answer = "SAT"
    elif day % 7 == 3:
        answer = "SUN"
    elif day % 7 == 4:
        answer = "MON"
    elif day % 7 == 5:
        answer = "TUE"
    elif day % 7 == 6:
        answer = "WED"
    elif day % 7 == 0:
        answer = "THU"

    return answer
