n, m = map(int, input().split());
card_num = list(map(int, input().split()));

total = 0;
answer = 0;

card_num.sort();

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            total = card_num[i] + card_num[j] + card_num[k]
            if total <= m:
                answer = max(answer, total)
print(answer);
