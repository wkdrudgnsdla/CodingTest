def solution(intStrs, k, s, l):
    result = []
    for st in intStrs:
        substr = st[s:s+l]
        if len(substr) != l: 
            continue
        val = int(substr)
        if val > k:
            result.append(val)
    return result
