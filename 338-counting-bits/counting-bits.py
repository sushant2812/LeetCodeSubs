class Solution:
  

    def countBits(self, n: int) -> List[int]:
        def countones(num):
            cnt=0
            while num!=0:
                num&=(num-1)
                cnt+=1
            return cnt

        a=[0]
        for i in range(1,n+1):
            a.append(countones(i))
        return a