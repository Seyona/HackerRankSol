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


twoStrings("car", "bar")
