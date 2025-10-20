def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    A_idx = 0
    B_idx = 0
    for i in range(len(A)):
        if A[A_idx] < B[B_idx]:
            A_idx += 1
            B_idx += 1
            answer += 1
        else:
            B.pop()
            A_idx += 1
    return answer