a=int(input())
if(a%2==0):
    odd(a-1)
else:
    odd(a)
    
def odd(n):
    l1=[]
    count=0
    i=1
    while(count<n):
        l1.append(i)
        i=i+2
        count=count+1
        
    print(l1)
