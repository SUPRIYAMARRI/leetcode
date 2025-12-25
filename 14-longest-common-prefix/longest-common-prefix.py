class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result=""
        for i in range(len(strs[0])):
            b=strs[0][i]
            for j in range(1,len(strs)):
                if i>=len(strs[j])or b!=strs[j][i]:
                    return result
            result=result+b          
        return result









        