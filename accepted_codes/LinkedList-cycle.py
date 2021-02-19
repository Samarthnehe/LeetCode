class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or head.next==None:
            return False
        temp=head
        curr=head
        while(curr and temp and temp.next):
            curr=curr.next
            temp=temp.next.next
            if(curr==temp):
                return True
        
        return False
