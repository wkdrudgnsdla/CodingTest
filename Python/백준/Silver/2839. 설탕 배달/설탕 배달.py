a = int(input())
count = 0

while True:
    if a == 0:
        break;
    elif a >= 5 and a % 5 == 0:
        a -= 5
        count += 1
    elif a >= 3:
        a -= 3
        count += 1
    else:
        count = -1
        break;
print(count)
    