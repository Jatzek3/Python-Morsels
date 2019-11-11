from collections import Counter
from collections import defaultdict


# def is_anagram1(word1,word2):
#     c1 = Counter(word1.upper())
#     c2 = Counter(word2.upper())
#     return c1 == c2


# def is_anagram2(word1, word2):
#     count1 = {}
#     count2 = {}
#     for item in word1.upper():
#         if item not in count1:
#             count1[item] = 0
#         count1[item] += 1
#     for item in word2.upper():
#         if item not in count2:
#             count2[item] = 0
#         count2[item] += 1
#     return (count1 == count2)
#
#
# def is_anagram3(word1, word2):
#     word1 = word1.upper()
#     word2 = word2.upper()
#     count1 = defaultdict(int)
#     count2 = defaultdict(int)
#     for i in word1:
#         count1[i] += 1
#     for i in word2:
#         count2[i] += 1
#     return count1 == count2
