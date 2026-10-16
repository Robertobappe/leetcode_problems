def twoSum (nums, target):
    for i in range(len(nums)):
            dif = target - nums[i]

            if dif in nums:
                j = nums.index(dif)
                if i !=j:
                    return [i,j]



nums = [[2,7,11,15], [3,2,4], [3,3]]
target = [9, 6, 6] 

for k in range(len(nums)):
    print(f'resultado {twoSum(nums[k], target[k])}')



'''
for i in range(len(nums)-1):
        for j in range(1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
'''