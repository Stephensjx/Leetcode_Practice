#1.Two Sum
def twoSum(nums, target):
    dic = {}
    for index, num in enumerate(nums):
        if target - num in dic:
            return [dic[target-num], index]
        else:
            dic[num] = index


case = twoSum([2, 7, 11, 15], 9)

#2.Add Two Numbers
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(0)
    l3 = head
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        if carry:
            l3.val = carry % 10
            l3.next = ListNode(0)
            l3 = l3.next
        carry = carry // 10
    return head
