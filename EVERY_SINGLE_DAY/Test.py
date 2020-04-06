#1.Two Sum
def twoSum(nums, target):
    dic = {}
    for index, num in enumerate(nums):
        if target - num in dic:
            return [dic[target-num], index]
        else:
            dic[num] = index


case = twoSum([2, 7, 11, 15], 9)
