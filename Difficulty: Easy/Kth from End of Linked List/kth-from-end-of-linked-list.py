class Solution:
    def getKthFromLast(self, head, k):
        temp=head
        res=[]
        while(temp):
            res.append(temp.data)
            temp=temp.next
        if(k>len(res)):
            return -1
        return res[-k]