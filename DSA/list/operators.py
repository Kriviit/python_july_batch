print("====concat===")
arr1=[1,2,3]
arr2=[4,5,6]
arr3=arr1+arr2
print(arr1)
print(arr2)
print(arr3)



print("====repeatition===")
arr1=[1,2,3]
arr2=arr1*3
print(arr2)

print("====indexing===")
arr=[1,2,3,4,55,[2,3,4],56,6]
print(arr[0])
print(arr[-1])
print(arr[-2])
print(arr[5][1])
arr[0]=30
print(arr)

print("====slicing===")
arr=[1,2,3,4,5,6,7,78,8,9,4,4,99]
sub=arr[2:7]
print(sub)
print(arr[4:])
print(arr[:7])