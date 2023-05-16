#1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    pos=[i,j]
                    break
        return(pos)
#9. Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        return(x[::-1]==x)