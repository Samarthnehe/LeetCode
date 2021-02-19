class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        temp=head
        curr=head
        it=head
        while(temp and curr and temp.next):
            curr=curr.next
            temp=temp.next.next
            if(curr==temp):
                while(it!=curr):
                    it=it.next
                    curr=curr.next
                return curr        
        return 
