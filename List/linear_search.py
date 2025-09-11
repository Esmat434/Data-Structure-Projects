def linear_search(lst,target):
    for i in lst:
        if i == target:
            return f"{target} Found in list"
    return f"{target} not found in list"

print(linear_search([1,2,3,4,5,6,7,8],6))