#another solution is same as largest solution
def get_second_smallest(nums):
   largest = nums[0]
   second_smallest = nums[0]
   for i in range(1,len(nums)):
       if nums[i] < largest:
           second_smallest = largest
           largest = nums[i]
       elif nums[i] < second_smallest:
           second_smallest = nums[i]
   return second_smallest
    
a=[15,58,96,12,45,65,98,78,25]
print(get_second_smallest(a))