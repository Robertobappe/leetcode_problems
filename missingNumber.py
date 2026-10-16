def missingNumber(nums):
    tam = len(nums)
    nums = set(nums)

    for i in range(tam):
        if i not in nums:
            return i
    return tam   


L = [[3,0,1], [0,1], [9,6,4,2,3,5,7,0,1]]
for i in L:
    print(missingNumber(i))     