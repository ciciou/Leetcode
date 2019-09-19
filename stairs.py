class Solution():
    def Stairs(self,f:int)->int:
        if f==1:
            return 1
        if f==2:
            return 2
        a,b=1,2
        i=3
        while f>=i:
            a,b=b,a+b
            i=i+1
        return b
if __name__=='__main__':
    print(Solution().Stairs(f=10))