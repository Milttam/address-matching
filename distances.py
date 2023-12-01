# !pip install polyleven
from polyleven import levenshtein
import scipy
import numpy
# import sklearn
from math import floor, ceil


def distance_jaccard(str1, str2):
    # find the jaccard distance between two strings
    str1 = set(str1.split())
    str2 = set(str2.split())
    return float(len(str1 & str2)) / len(str1 | str2)


def jaro_distance(s1, s2):
    # if the strings are equal
    if (s1 == s2):
        return 1.0

    # length of two strings
    len1 = len(s1)
    len2 = len(s2)

    if (len1 == 0 or len2 == 0):
        return 0.0

    # maximum distance upto which matching
    # is allowed
    max_dist = (max(len(s1), len(s2)) // 2) - 1

    # count of matches
    match = 0

    # hash for matches
    hash_s1 = [0] * len(s1)
    hash_s2 = [0] * len(s2)

    # traverse through the first string
    for i in range(len1):
        # check if there is any matches
        for j in range(max(0, i - max_dist),
                       min(len2, i + max_dist + 1)):
            # if there is a match
            if (s1[i] == s2[j] and hash_s2[j] == 0):
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break

    # if there is no match
    if (match == 0):
        return 0.0

    # number of transpositions
    t = 0
    point = 0

    # count number of occurrences where two characters match but there is a third matched character in between the indices
    for i in range(len1):
        if (hash_s1[i]):

            # find the next matched character in second string
            while (hash_s2[point] == 0):
                point += 1

            if (s1[i] != s2[point]):
                point += 1
                t += 1
            else:
                point += 1

        t /= 2

    # return the jaro similarity
    return ((match / len1 + match / len2 +
            (match - t) / match) / 3.0)

# jaro winkler similarity


def distance_jaro_winkler(s1, s2):

    jaro_dist = jaro_distance(s1, s2)

    # if the jaro similarity is above a threshold
    if (jaro_dist > 0.7):

        # find the length of common prefix
        prefix = 0

        for i in range(min(len(s1), len(s2))):

            # if the characters match
            if (s1[i] == s2[i]):
                prefix += 1
            else:
                break

        # maximum of 4 characters are allowed in prefix
        prefix = min(4, prefix)

        # calculate jaro winkler similarity
        jaro_dist += 0.1 * prefix * (1 - jaro_dist)

    return jaro_dist
