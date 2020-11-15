# https://www.hackerrank.com/interview/interview-preparation-kit/dictionaries-hashmaps/challenges


# Problem: Ransom Note
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def checkMagazine(magazine, note):
    posWords = {}
    for word in magazine:
        if word in posWords:
            posWords[word] += 1
        else:
            posWords[word] = 1

    for word in note:
        if word in posWords:
            if posWords[word] == 0:
                print("No")
                return
            else:
                posWords[word] -= 1

    # There is a cheeky solution using collections.Counter
    # return not (Counter(note) - Counter(magazine))

    print("Yes")


# Problem: Two strings
# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def twoStrings(s1, s2):
    setS1 = set(s1)
    setS2 = set(s2)

    if setS1.intersection(setS2):  # if there is a set of common elements there is one, or more, common substring
        return "YES"

    return "NO"


# Problem: Sherlock and Anagrams
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
from collections import Counter # not best practice to put an import here, but makes it easier to see what I am using for a given problem


def sherlockAndAnagrams(s):
    buckets = {}
    length = len(s)
    for i in range(length):
        for j in range(1, length - i + 1):
            key = frozenset(Counter(s[i:i + j]).items()) # Sets can't be hashed use frozen set.
            buckets[key] = buckets.get(key, 0) + 1

    anagrams = 0
    for key in buckets:
        anagrams += buckets[key] * (buckets[key] - 1) // 2

    return anagrams

# Problem: Count Triplets
# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

"""
    Why does this work?
    - The problem description lets us assume that the list will be sorted from lowest to highest
    - While iterating we add each value to the dictionary (with the key being the value we are iterating over)
    - If we hit the scenario where the current value * r exists in the dictionary we know we potentially hit a triple
    
    ex: countTriplets([1,2,2,4],2)
    loop1: 4 gets added to the tripDict
    loop2: 2 * 2 = 4, Potential triple found, tripDictPairs[2] is created and assigned to the value of tripDict[i*r]
    loop3: 2* 2 = 4, Potential triple found again, tripDictPairs[2] gets tripDict[i*r] added to it
    loop4: 1* 2 = 2, tripDictPairs has a key of 2, so we add that key's value to the number of triples
    
    If there was another 4 in the passed list we'd have a total of 4 triples instead of 2. 
    
"""
def countTriplets(arr, r):
    triplets = 0

    tripDict = {}
    tripDictPairs = {}

    for i in reversed(arr):
        if i*r in tripDictPairs:
            triplets += tripDictPairs[i * r]
        if i*r in tripDict:
            tripDictPairs[i] = tripDictPairs.get(i, 0) + tripDict[i*r]

        tripDict[i] = tripDict.get(i, 0) + 1

    return triplets
