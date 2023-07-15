class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 当前指针，结果链表
        result = curr = ListNode()
        # 进位项
        remainder = 0

        # 非空满足循环条件
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + remainder

            curr.next = ListNode(total % 10)
            remainder = total // 10

            # 🚩防止某一链表已经为空，空链表.next会报错
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next

        if remainder:
            curr.next = ListNode(remainder)
        return result.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2

    node11 = ListNode(2)
    node22 = ListNode(9)
    node11.next = node22

    def printList(node):
        while node:
            print(node)
            node = node.next

    # printList(node1)
    # printList(node11)

    obj = Solution()
    # list1 = [1, 2]
    # list2 = [2, 9]
    printList(obj.addTwoNumbers(node1, node11))

    # output    
