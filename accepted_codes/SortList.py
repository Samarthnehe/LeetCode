class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def findMid(head,tail):
            fast=head
            slow=head
            while(fast!=tail and fast.next!=tail):
                fast=fast.next.next
                slow=slow.next
            return slow
        def mergeSort(lh,rh):
            if not lh:
                return rh
            elif not rh:
                return lh
            elif lh.val<=rh.val:
                lh.next=mergeSort(lh.next,rh)
                return lh
            else:
                rh.next=mergeSort(lh,rh.next)
                return rh
        def merge(head,tail):
            if(head==tail):
                br=ListNode(head.val)
                return br
            mid=findMid(head,tail)
            lh=merge(head,mid)
            rh=merge(mid.next,tail)
            cl=mergeSort(lh,rh)
            return cl
        if not head or not head.next:
            return head
        temp=head
        curr=head
        while(temp.next):
            temp=temp.next
        return merge(curr,temp)
