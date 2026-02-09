class Solution(object):
    def maxProduct(self, nums):
      product=nums[0]
      max_product=nums[0]
      min_product=nums[0]
      for i in range(1,len(nums)):
        if nums[i]<0:
          max_product,min_product=min_product,max_product
        max_product=max(nums[i],max_product*nums[i])
        min_product=min(nums[i],max_product*nums[i])
        product=max(product,max_product)
      return product
        
