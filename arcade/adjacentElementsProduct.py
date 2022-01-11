def solution(inputArray):
    lst1 = 0
    for i in range(0, len(inputArray)-1):
        lst2 = inputArray[i] * inputArray[i+1]
        if lst2 > lst1:
            lst1 = lst2
    return lst1