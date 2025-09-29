def solution(ingredient):
    answer = 0
    stack = []
    correct_burger = [1, 2, 3, 1]
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == correct_burger:
            for _ in range(4):
                stack.pop()
            answer += 1
    return answer