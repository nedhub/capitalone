def solution(inputArray):
    m = len(max(inputArray, key=len))
    return [s for s in inputArray if len(s) == m]

# Given an array of strings, return another array containing all of its longest strings.