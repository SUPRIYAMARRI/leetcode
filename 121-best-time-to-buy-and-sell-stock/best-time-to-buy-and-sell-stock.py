class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=prices[0]
        c=0
        for i in range(1,len(prices)):
            if prices[i]<a:
                a=prices[i]
            else:
                b=prices[i]-a
                if b>c:
                    c=b
        return c        
                


        




        