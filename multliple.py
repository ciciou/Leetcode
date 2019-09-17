#-*-coding: utf-8 -*-
#author:cici
from typing import List
class Solution:
    def FindMaxLenNumSeq(self,str)->List[int]:
        numlist1 = []
        numlist2 = []
        for char in str:
            try:
                int(char)
                numlist1 += char
            except:
                if len(numlist2) > len(numlist1):
                    pass
                else:
                    numlist2 = numlist1
                    numlist1 = []
        return numlist2
if __name__ == '__main__':
    str = "012k35abc12defg3546xyz12"
    print(Solution().FindMaxLenNumSeq(str=str))