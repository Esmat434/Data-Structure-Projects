def binary_search(lst,target):
    if not lst:
        return False
        
    mid = len(lst) // 2
    
    if lst[mid] == target:
        return True
    elif lst[mid]<target:
        return binary_search(lst[mid+1:],target)
    else:
        return binary_search(lst[:mid],target)

n = [1,2,3,4,5,6,7,8,9]
print(binary_search(n,20))