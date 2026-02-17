class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a=sorted(score)
        a.reverse()
        d={}
        for i,s in enumerate(a):
            if i==0:
                d[s]="Gold Medal"
            elif i==1:
                d[s]="Silver Medal"
            elif i==2:
                d[s]="Bronze Medal"
            else:
                d[s]=str(i+1)
        result=[]
        for j in score:
            result.append(d[j])
        return result


        