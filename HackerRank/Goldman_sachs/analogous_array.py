def countAnalogousArrays(consecutiveDifference, lowerBound, upperBound):
    if len(consecutiveDifference) == 0:
        return 0

    if upperBound < lowerBound :
        return 0
    minEdgePoint = float('-inf')
    maxEdgePoint = float('inf')
    currentIter = 0

    for diff in consecutiveDifference:
        currentIter+=diff
        if currentIter > minEdgePoint:
            minEdgePoint = currentIter

        if currentIter < maxEdgePoint:
            maxEdgePoint = currentIter

        if(upperBound+maxEdgePoint < upperBound):
            validupperbound = upperBound + maxEdgePoint
        else:
            validupperbound = upperBound

        if(lowerBound + minEdgePoint):
            validlowerbound = lowerBound + minEdgePoint
        else:
            validlowerbound = lowerBound

    if validupperbound >= validlowerbound:
        return validupperbound - validlowerbound + 1
    else:
        return 0


if __name__ == '__main__':
    
    # Defines the length of the difference array
    cons_diff_len = int(input())
    consecutiveDifference = []

    for elem in range(cons_diff_len):
        consecutiveDifference.append(int(input()))
    
    lowerBound = int(input())
    upperBound = int(input())

    out_val = countAnalogousArrays(consecutiveDifference, lowerBound, upperBound)
    print(out_val)

