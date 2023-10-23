from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newListNode = ListNode()
        submitList = []
        if list1.val < list2.val:
            submitList.append(list1.val)
        else:
            submitList.append(list2.val)
        return submitList
    
class Testing:
    def testOne(self):
        exampleNode = ListNode(1, ListNode(3, ))
        list1 = [1, 3, 5, 7]
        list2 = [1, 2, 3, 4]
        mergedList = [1, 1, 2, 3, 3, 4, 5, 7]
        solution = Solution()
        # attempt = solution.mergeTwoLists(list1, list2)
        print("The first list was " + str(list1))
        print("The second list was " + str(list2))
        print("The solution is " + str(mergedList))
        # print(attempt.val)
        return 
    def createLinkedList(self, array):
        for item in array:
            ListNode(item, )
    
testing = Testing()    
testing.testOne()