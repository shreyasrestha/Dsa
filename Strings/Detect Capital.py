#Problem: Detect Capital
#Platform: LeetCode (520)
#Difficulty: Medium
#Topic: String

#Time complexity = O(n)
#Space complexity = O(n)

def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
            return True

        return False
