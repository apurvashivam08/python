# def get_second_largest(num):
#     num.remove(max(num))
#     return max(num)
def get_second_largest(nums):
   largest = nums[0]
   second_largest = nums[0]
   for i in range(1,len(nums)):
       if nums[i] > largest:
           second_largest = largest
           largest = nums[i]
       elif nums[i] > second_largest:
           second_largest = nums[i]
   return second_largest
    
a=[15,58,96,12,45,65,98,78,25]
print(get_second_largest(a))