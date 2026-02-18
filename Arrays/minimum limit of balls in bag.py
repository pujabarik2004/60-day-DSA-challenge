class Solution(object):
    def minimumSize(self, nums, maxOperations):
        low=1
        high=max(nums)
        while low<high:
            mid=(low+high)//2
            operation=0
            for balls in nums:
                operation+=(balls-1)//mid
            if operation>maxOperations:
                low=mid+1
            else:
                high=mid
        return low
        
