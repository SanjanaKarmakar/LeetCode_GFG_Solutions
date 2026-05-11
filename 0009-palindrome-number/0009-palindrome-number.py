class Solution(object):
    def isPalindrome(self, n):
        m=n
        s= 0
        while n>0:
            r=n%10
            s= s*10+r
            n= n//10
        if m==s:
            return True
        else:
            return False
