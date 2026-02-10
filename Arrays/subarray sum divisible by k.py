class solution(object):
  def subarraydivbyk(self,nums,k):
    rem_count={0:1}
    curr_sum=0
    count=0
    
    for num in nums:
        curr_sum+=num
        remainder=curr_sum%k
      
      #this is for negative remainder(edge case):
        if remainder<0:
            remainder+=k
       #this count the how many time same remainder occurs:   
        if remainder in rem_count:
            count+=rem_count[remainder]
       #store the count in hashmap for future: 
        if remainder in rem_count:
            rem_count[remainder]+=1
        else:
            rem_count[remainder]=1
     return count
