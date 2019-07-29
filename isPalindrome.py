#-*-coding: utf-8 -*-
#author:cici
class Solution():
    def isPalindrome(self,x:int)->bool:
        #思路：python内置函数反转
        y=int(''.join(reversed(str(x))))
        if x<0:
            return False
        else:
            return True if x==int(''.join(reversed(str(x)))) else False

    def isPalindrome_1(self,x:int)->bool:
        #思路：切分反转[::-1]
        if x<0:
            return False
        else:
            return True if x==str(x[::-1]) else  False
if __name__=='__main__':
    x=1221
    print(Solution().isPalindrome(x=x))