def reverseList(head):
        
        n = len(head)
        
        i = 0
        half = n/2
        n = n-1
                
        while i < half:

            head[i], head[n-i] == head[n-i], head[i]
            i+=1
    
        return head
            

test = [1,2,3,4]
reverseList(test)