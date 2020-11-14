# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairDic = {}
    pairs = 0
    for i in ar:
        if i not in pairDic:
            pairDic[i] = i
        else:
            pairs += 1
            pairDic.pop(i, None)
    return pairs


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    currentLevel = 0  # 0 is start of sea level
    numValley = 0
    for step in path:
        if step == 'D':
            currentLevel -= 1
        elif step == 'U':
            if currentLevel == -1:  # Next step will put us at sea level
                numValley += 1
            currentLevel += 1
    return numValley


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    stack = []

    i = 0
    while i < len(c) - 1:
        if c[i] == 0 and c[i + 1] == 1:
            jumps += 1
            i += 2
            stack = []
        else:
            if len(stack) == 0:
                stack.append(0)
                jumps += 1
            else:
                stack = []
            i += 1

    return jumps


# Complete the repeatedString function below.
def repeatedString(s, n):
    remainder = n % len(s)
    divides = n // len(s)  # Floor division

    numAs = s.count("a") * divides + s[:remainder].count("a")
    """
    numAs = 0
    for i in range(0, len(s)):
        if s[i] == "a":
            numAs += 1

    numAs *= divides
    for i in s[:remainder]:
        if i == "a":
            numAs += 1
    """
    return numAs
