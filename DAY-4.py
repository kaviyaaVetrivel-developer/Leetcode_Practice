class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        original_num=num
        palindrome_num=0
        while num>0:
            digit= num%10
            num=num//10
            palindrome_num=palindrome_num*10+digit

                  
        if original_num == palindrome_num:
            return True
        else:
            return False