x= int(input())
y = int(input())
z= int(input())
n = int(input())

diff=[]
diff.append(x-n)
diff.append(y-n)
diff.append(z-n)
if diff[0]>=0 and diff[1]<0 or diff[1] >diff[0] and diff[2]<0 or diff[2]>diff[0]:
    print("L1")
elif diff[1]>=0 and diff[0]<0 or diff[0] >diff[1] and diff[2]<0 or diff[2]>diff[1]:
    print("L2")
elif diff[2]>=0 and diff[1]<0 or diff[1] >diff[2] and diff[0]<0 or diff[0]>diff[2]:
    print("L3")

