n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
merged_array = []
i = 0
j = 0
 
while i < n and j < m:
    if arr1[i] <= arr2[j]:
        merged_array.append(arr1[i])
        i += 1
    else:
        merged_array.append(arr2[j])
        j += 1
 
while i < n:
    merged_array.append(arr1[i])
    i += 1
 
while j < m:
    merged_array.append(arr2[j])
    j += 1
 
print(*merged_array)
