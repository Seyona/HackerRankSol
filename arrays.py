# https://www.hackerrank.com/interview/interview-preparation-kit/arrays/challenges

import sys

def hourglassSum(arr):
    maxSum = -sys.maxsize - 1
    for i in range(1, 5):  # Index 0 and 5 cannot have an hour glass
        for j in range(1, 5):
            topRowSum = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1]
            centerRow = arr[i][j]
            botRowSum = arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1]
            overallSum = topRowSum + centerRow + botRowSum

            if overallSum > maxSum:
                maxSum = overallSum

    return maxSum


def rotLeft(a, d):
    rotations = d % len(a)
    return a[rotations:] + a[:rotations]


def minimumBribes(q):
    swaps = 0
    pos1, pos2, pos3 = 1, 2, 3
    for i in range(0, len(q)):
        if q[i] == pos1:
            pos1 = pos2
            pos2 = pos3
            pos3 += 1
        elif q[i] == pos2:
            swaps += 1
            pos2 = pos3
            pos3 += 1
        elif q[i] == pos3:
            swaps += 2
            pos3 += 1
        else:
            return "Too chaotic"
    return swaps

def minimumSwaps(arr):
    swaps = 0
    for i in range(0, len(arr)):
        while arr[i] != i + 1: # keep swapping until we get the expected value for this index
            curVal = arr[i]
            swapVal = arr[curVal - 1]
            arr[i] = swapVal
            arr[curVal - 1] = curVal
            swaps += 1

    return swaps


def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for query in queries:
        firstInd = query[0]-1
        secondInd = query[1]
        value = query[2]

        # We subtract the value from the second index so when the running total
        # is calculated the prior values do not get double counted
        arr[firstInd] += value
        arr[secondInd] -= value

    maxv = 0
    runningTotal = 0
    for i in arr:
        runningTotal += i
        if runningTotal > maxv:
            maxv = runningTotal

    return maxv
