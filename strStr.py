#-*-coding: utf-8 -*-
#author:cici
class Solution():
    def strStr(self,haystack:str,needle:str)->int:
        #思路：find()检查字符串中是否包含子字符串str
        if needle==[]:
            return -1
        else:
            if needle in haystack:
                return haystack.find(needle)
            else:
                return -1
if __name__=='__main__':
    haystack='hello'
    needle='ll'
    print(Solution().strStr(haystack=haystack,needle=needle))




