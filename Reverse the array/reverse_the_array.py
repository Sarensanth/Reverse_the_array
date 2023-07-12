def reverse(array):
    i=0
    j=len(array)-1
    while i<j:
        array[i],array[j]=array[j],array[i]
        i+=1
        j-=1
    return array

array=list(map(int,input().split()))
print(reverse(array))