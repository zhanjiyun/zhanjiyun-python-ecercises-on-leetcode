from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 将输入的列表转换为链表
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# 链表结果打印为列表
def print_linkedlist(node):
    list=[]
    while node:
        list.append(node.val)
        node = node.next
    return list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        tail = head
        carry = 0
        while l1 or l2 or carry:
            if  l1 :
                carry+=l1.val
                l1 = l1.next
            if  l2 :
                carry+=l2.val
                l2 = l2.next
            tail.next = ListNode(carry%10)
            carry //= 10
            tail = tail.next

        return head.next

if __name__ == '__main__':
    s = Solution()
    l1_list = eval(str(input()))
    l2_list = eval(str(input()))
    l1 = list_to_linkedlist(l1_list)
    l2 = list_to_linkedlist(l2_list)

    # 测试集
    # l1 = list_to_linkedlist([2, 4, 3])
    # l2 = list_to_linkedlist([5, 6, 4])

    result = s.addTwoNumbers(l1, l2)
    print(print_linkedlist(result))