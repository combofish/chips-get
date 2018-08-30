#!/usr/bin/env python
#-*- coding:utf-8 -*-







"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
"""
#        :type s: str
#        :rtype: int

"""
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2
        sub_dir = {}
        
        max_length = 0
        st = 0
        end = 0
        
        for i in range(len(s)):
            end = i
            if s[i] in sub_dir and st <= sub_dir[s[i]]:
                temp_length = (end - st)
                st = sub_dir[s[i]] + 1
                if temp_length > max_length:
                    max_length = temp_length
                
                
            sub_dir[s[i]] = i
            
        temp_length = (end - st) + 1
        if temp_length > max_length:
            max_length = temp_length
        return max_length
if __name__ == '__main__':
    du = Solution()
    print(du.lengthOfLongestSubstring("abcabcbc"))
"""
        
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        ptr1 = 0
        ptr2 = 0
        maps = {}
        maxx = 0
        
        while ptr2 < len(s):
            nextChar = s[ptr2:ptr2+1]
            if nextChar in maps:
                steps = ptr2 - ptr1
                maxx = max(steps,maxx)
                    
                ptr1 += 1
                ptr2 = ptr1
                maps = {}

            else:
                maps[nextChar] = 1
                ptr2 += 1
                
        steps = ptr2 - ptr1
        maxx = max(steps,maxx)
        
        return(maxx)
"""
    
"""
def addTwoNumber(li,lj):
    x,y=0, 0
    sign=1
    for i in range(len(li)):
        x = x + li[i] * sign
        y = y + lj[i] * sign
        sign=sign * 10
    return x+y
print(addTwoNumber([2,4,3],[5,6,4]))
"""

"""
def sumTwo(li,target):
    for i in range(len(li)):
        n = target - li[i]
        for j in range(len(li)):
            if j == i :
                continue
            if li[j] == n :
                return (i,j)
    return 0

print('j')
print(sumTwo([2,7,7,11,15,15],14))
"""

"""
l=[2,7,11,15]
print(l[0])
"""

"""
def fibonacci():
    a,b = 0,1
    while True:
        yield b
        a,b = b, a+b
fib= fibonacci()
print([fib.next() for i in range(10)]) 
if __name__ == '__main__':
    fib=fibonacci()
    print(fib.next())
"""
    
"""
class MyIterator(object):
    def __init__(self,step):
        self.step = step
    def next(self):
        if self.step == 0:
            raise StopIteration
        self.step -=1
        return self.step
    def __iter__(self):
        return self
for el in MyIterator(4):
    print(el)
"""    

"""
def use(n):
    pass
"""

"""
def fact_large2(n):
    result = 1
    for i in range(n):
        result = result * (i +1)
    return result
print(fact_large2(1000))
    

def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
print(fact(10))

l=[]
l.append('liingj')
l.append(1)
print(l)
l.pop(1)
print(l)
a='liming'
b=a.replace('i','I')
print(b)
print(a)
g=['a','v','e','t']
print(g)
g.sort()
print(g)
d={'liming':1,"haha":3}
print(d.get('liming'))
d.pop("haha")
print("haha" in d)
a=(0,)
print(len(a))
print(len('haha'))
print('''ahha
j
def man(self):
    return 'haha'
if __name__ == "__main__":
    print(man())
    man()''')
"""
