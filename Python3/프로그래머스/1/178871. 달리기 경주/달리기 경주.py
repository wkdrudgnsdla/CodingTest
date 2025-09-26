def solution(players, callings):
    tempdic = {}
        
    for i in range(len(players)):
         tempdic[players[i]] = i
            
    callPlayeridx = 0
    for i in range(len(callings)):
        callPlayeridx = tempdic[callings[i]]
        tempdic[players[callPlayeridx]], tempdic[players[callPlayeridx-1]] =  tempdic[players[callPlayeridx-1]], tempdic[players[callPlayeridx]]
        
        
        players[callPlayeridx], players[callPlayeridx - 1] = players[callPlayeridx - 1], players[callPlayeridx]
    answer = players
    return answer