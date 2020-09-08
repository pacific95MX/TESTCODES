n=int(input("Enter the number of element in list"))
list1=[]
for i in range(0,n):
    a=int(input())
    list1.append(a)
c1=c2=c3=c4=c5=c6=c7=c8=c9=0
for i in list1:
    if(i==0):
        continue
    if(i%1==0):
        c1=c1+1
    if(i%2==0):
        c2=c2+1
    if(i%3==0):
        c3=c3+1
    if(i%4==0):
        c4=c4+1
    if(i%5==0):
        c5=c5+1
    if(i%6==0):
        c6=c6+1
    if(i%7==0):
        c7=c7+1
    if(i%8==0):
        c8=c8+1
    if(i%9==0):
        c9=c9+1
d1={}
d1[1]=c1
d1[2]=c2
d1[3]=c3
d1[4]=c4
d1[5]=c5
d1[6]=c6
d1[7]=c7
d1[8]=c8
d1[9]=c9
print(d1)
