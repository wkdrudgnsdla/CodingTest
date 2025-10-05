def solution(numbers):
    answer = 0
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    answer = max1 * max2
    return answer