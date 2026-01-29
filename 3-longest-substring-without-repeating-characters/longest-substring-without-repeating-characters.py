class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=""
        max_len=0
        for i in s:
            if i in a:
                a=a[a.index(i)+1:]
            a+=i
            max_len=max(max_len,len(a))
        return max_len
        