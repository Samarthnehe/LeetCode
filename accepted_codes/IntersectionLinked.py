class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp=headA
        temp1=headB
        if not headA or not headB:
            return 
        length1=1
        while(temp.next):
            temp=temp.next
            length1+=1
        length2=1
        while(temp1.next):
            temp1=temp1.next
            length2+=1
        curr1=headA
        curr2=headB
        diff=abs(length2-length1)
        if(length1>=length2):
            for i in range(diff):
                curr1=curr1.next
            while(curr1 and curr2 and curr1!=curr2):
                curr1=curr1.next
                curr2=curr2.next
    
        else:
            for i in range(diff):
                curr2=curr2.next
            while(curr1 and curr2 and curr1!=curr2):
                curr1=curr1.next
                curr2=curr2.next
        
        if(curr1 and curr2 and curr1==curr2):
            return curr1
        else:
            return 
