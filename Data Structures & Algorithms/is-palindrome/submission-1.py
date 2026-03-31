class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=""
        for i in s:
            if i.isalnum():
                result+=i.lower()
        i=0
        j=len(result)-1
        while i<j:
            if result[i] != result[j]:
                return False
            i+=1
            j-=1
        return True