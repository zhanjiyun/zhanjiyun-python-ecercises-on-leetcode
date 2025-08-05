from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()  # 哑节点
        dummy.next = head

        # current = head
        # size = 0
        # while current:  # 获取链表长度
        #     current = current.next
        #     size += 1
        # loc = size - n  # head中正着数第几个节点，从0计数
        #
        # current = dummy
        #
        # for i in range(loc):  # 从哑节点开始循环loc遍
        #     current = current.next
        # # 循环结束时在要删除的节点的前驱节点
        # current.next = current.next.next
        # return dummy.next

        # 快慢双指针
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next


# 将输入的列表转换为链表
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next  # 返回的是链表的头节点


# 链表结果打印为列表
def print_linkedlist(node):
    list = []
    while node:
        list.append(node.val)
        node = node.next
    return list


if __name__ == '__main__':
    s = Solution()
    lst = [1, 2, 3, 4, 5]
    n = 2
    ls = list_to_linkedlist(lst)
    print(print_linkedlist(s.removeNthFromEnd(ls, n)))

    # 反转链表
    # def reversed_linkedlist(node: Optional[ListNode]):
    #     prev = None  # 初始前驱为None
    #     current = node
    #     while current:
    #         next = current.next  # 暂存下一节点
    #         current.next = prev  # curr指向前驱
    #         prev = current  # 更新前驱，curr是next的前驱
    #         current = next
    #     return prev
    #
    # print(print_linkedlist(reversed_linkedlist(ls)))
