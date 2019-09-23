#-*-coding: utf-8 -*-
#author:cici
from typing import List
class Solution():
    def max_drowdown(self,arry:List[int]):
        assert len(arry)>2,"len(arry) should >2"
        x,y=arry[0:2]
        xmax=x
        maxdiff=x-y
        for i in range(2,len(arry)):
            if arry[i-1]>xmax:
                xmax=arry[i-1]
            if xmax-arry[i]>maxdiff:
                maxdiff=xmax-arry[i]
                x,y=xmax,arry[i]
        print("x=",x,"y=",y)
        return maxdiff
if __name__=='__main__':
    print(Solution().max_drowdown(arry=[3,7,2,6,4,1,9,8,5]))