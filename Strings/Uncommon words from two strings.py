#Problem: Uncommon Words from two strings
#Platform: LeetCode
#Difficulty: Easy
#Topic: String

#Approach 1 
#Time complexity = O(n^2 + m^2)



def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.strip().split(" ")
        s2=s2.strip().split(" ")
        res=[]
        for i in s1:
            if i not in s2 and s1.count(i)==1:
                res.append(i)
        for j in s2:
            if j not in s1 and s2.count(j)==1:
                res.append(j)

        return res

#Approach 2 (Using Counter)
#Time complexity = O(n+m)

from collections import Counter

def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    count = Counter(s1.split()) + Counter(s2.split())
    return [word for word in count if count[word] == 1]

#Approach 3 (Using Dictionary)
#Time complexity = O(n+m)

def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    freq = {}

    for word in s1.split():
        freq[word] = freq.get(word, 0) + 1

    for word in s2.split():
        freq[word] = freq.get(word, 0) + 1

    res = []

    for word in freq:
        if freq[word] == 1:
            res.append(word)

    return res
