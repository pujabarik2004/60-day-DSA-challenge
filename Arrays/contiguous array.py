class solution(object):
  def contiguousarray(self,nums):
    prefix_sum={0:-1}
    curr_sum=0
    max_len=0
    for i in range(len(nums)):
      if nums[i]==0
        curr_sum-=1
      else:
        curr_sum+=1
      if curr_sum in prefix_sum:
        max=max(max_len,i-prefix_sum[curr_sum])
      else:
        prefix_sum[curr_sum]=i
    return max_len
