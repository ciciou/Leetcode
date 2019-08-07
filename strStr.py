#-*-coding: utf-8 -*-
#author:cici
class Solution():
    def strStr(self,haystack:str,needle:str)->int:
        #思路：调用库函数find()检查字符串中是否包含子字符串str
        if needle==[]:
            return -1
        else:
            if needle in haystack:
                return haystack.find(needle)
            else:
                return -1

    def strStr_1(self,haystack:str,needle:str)->int:
        #思路：暴力法，时间复杂度：O((m-n)n)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
            else:
                pass
        return -1
if __name__=='__main__':
    haystack='hello'
    needle='ll'
    print(Solution().strStr_1(haystack=haystack,needle=needle))




