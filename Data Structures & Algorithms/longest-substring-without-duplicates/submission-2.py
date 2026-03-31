class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i=0
        j=0
        count=0
        while j<len(s):
            if s[j] not in seen:
                seen.add(s[j])
                count = max(count,j-i+1)
                j+=1
            else:
                seen.remove(s[i])
                i+=1
        return count
        
