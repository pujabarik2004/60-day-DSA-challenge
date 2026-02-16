#betttersolution
class Solution(object):
  def findmin(self,nums):
      low=0
      high=len(nums)-1
      while low<high:
         mid=(low+high)//2
         if nums[mid]>nums[high]:
            low=mid+1
         elif nums[mid]<nums[high]:
             high=mid
         else:
            high=mid-1
      return nums[low]


#anothersolution(by taking extra variable that is mini): 
class Solution(object):
  def findmin(self,nums):
      low=0
      high=len(nums)-1
      mini=float('inf')
      while low<=high:
         mid=(low+high)//2
         if nums[mid]<=nums[high]:
            mini=min(mini,nums[mid])
            high=mid-1
         else:
            mini=min(mini,nums[low])
            low=mid+1
      return mini
