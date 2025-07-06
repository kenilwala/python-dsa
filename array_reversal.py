def reverseArray(arr):
    n=len(arr)
    #temporary array to store elements in it
    temp= [0]*n
    #Copy elements from original to temp in reeverse order
    for i in range(n):
        temp[i]=arr[n-i-1]
    #copy element back to original array
    for i in range(n):
        arr[i] = temp[i]
    
arr = [1,2,3,4,5,6,7,8,9]
#original array printing
for i in range(len(arr)):
    print(arr[i],end="")
#newline
print("")
#reversefunction
reverseArray(arr)
#reversed array printing
for i in range(len(arr)):
    print(arr[i],end="")