



def isPalindrome(self, s: str) -> bool:
        string=""
        for i in s.lower():
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                string+=i

        return string==string[::-1]
