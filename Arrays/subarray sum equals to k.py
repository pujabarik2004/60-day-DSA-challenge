class Solution(object):
    def subarraySum(self, nums, k):
        prefix_count={0:1}
        curr_sum=0
        count=0
        for num in nums:
            curr_sum+=num
            if curr_sum - k in prefix_count:
                count += prefix_count[curr_sum - k]
            if curr_sum in prefix_count:
                prefix_count[curr_sum]+=1
            else:
                prefix_count[curr_sum]=1
        return count
        
