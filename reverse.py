class Solution:
    def reverse(self,x:int)->int:
        #数值取余、累加
        y=abs(x)
        result=0
        while y>0:
            result=result*10+y%10
            y//=10
            if result < (1<<31)-1:
                result = result
            else:
                pass
        if x<0:
            return -result
        else:
            return result
    def reverse_1(self,x:int)->int:
        #python3内置函数（字符串反转+字符串拼接）
        if x<0:
            x=int(''.join(reversed(str(x)[1:])))
            if x<=-(1<<31)-1:
                return 0
            else:
                return -x
        else:
            x=int(''.join(reversed(str(x))))
            if x>=(1<<31)-1:
                return 0
            else:
                return x

    def reverse_2(self,x:int)->int:
        #python3内置函数（字符串反转+字符串左侧补零）
        return int(''.join(reversed(str(bin(x)[2:].zfill(32)))),2)

    def reverse_3(self,x:int)->int:
        result=0
        for n in range(32):
            index=x&1
            x>>=1
            result=result*2+index
        return result

if __name__=='__main__':
    x=-123
    print(Solution().reverse_3(x))