def solution(arr):
    stk = []
    idx = 0
    i = 0
    while i < len(arr):
        if not stk:
            stk.insert(idx,arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            elif stk[-1] >= arr[i]:
                del stk[-1]
    return stk