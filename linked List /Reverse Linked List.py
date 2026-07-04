#Problem: Reverse Linked List
#Platform: LeetCode
#Difficulty: Easy
#Topic: Linked List

#Iterative Approach
#Time Complexity=O(n)


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head

        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex

        return prev


