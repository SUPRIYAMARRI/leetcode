class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = []
        f = []
        for i in range(len(strs)):
            b = sorted(strs[i])
            if b in s:
                index = s.index(b)
                f[index].append(strs[i])
            else:
                s.append(b)
                f.append([strs[i]])

        return f
