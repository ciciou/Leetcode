class Solution:
    def reverse(self,x:int)->int:
        y=abs(x)
        result=0
        while y>0:
            result=result*10+y%10
            y//=10
        result=result if result < (1<<31)-1 else 0
        return -result if x<0 else result
if __name__=='__main__':
    x=120
    print(Solution().reverse(x))