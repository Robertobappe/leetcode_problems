def containsDuplicate(nums):
    s = set(nums)

    if len(s) == len(nums):
        return False
    return True


L = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
for i in L:
    print(containsDuplicate(i))