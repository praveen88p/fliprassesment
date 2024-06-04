import timeit


arr = [27, 54, 64, 68, 84, 100, 118, 129, 163, 175, 190, 204, 231, 238, 248, 271, 291, 319, 323, 355, 371, 387, 414, 422, 430, 441, 480, 498, 519, 536, 592, 593, 614, 632, 659, 675, 697, 701, 702, 721, 768, 785, 830, 853, 858, 896, 923, 946, 962, 991]

target = 962

def BS(arr, low, high, target):
    
    while(low<=high):
        mid =(low+high)//2
        
        if(arr[mid] == target):
            return (mid)
        
        elif(target > arr[mid]):
            low = mid + 1
            
        else: high = mid - 1
    
    return -1


time_taken = timeit.timeit(lambda: BS(arr, 0, len(arr)-1, target), number =10000 )

result = BS(arr, 0, len(arr)-1, target)

if result != -1 :
    print(f"Target is found at index :  {result}")

else :print("Target is not found in the array")

time_taken_rounded = round(time_taken, 5)

print(f"Time taken by iterative Binary search = {time_taken_rounded} seconds")

print("-----------------------------------------------------------\n")

#############################################################################################
## Recursive Binary Search

tar = 675

def bs(arr, Low, High, tar):
    if(Low>High):
        return -1
    
    Mid = (Low+High)//2
    
    if(arr[Mid] == tar):
        return Mid
    
    elif(tar>arr[Mid]):
        return bs(arr, Mid+1, High, tar)
    
    else:
        return bs(arr,Low, Mid-1, tar)
    
    
time_recursive = timeit.timeit(lambda: bs(arr, 0, len(arr)-1, target), number =10000 )

ans = bs(arr, 0, len(arr)-1, tar)

if ans != -1 :
    print(f"found target at index :  {ans}")

else :
    print("Target not found")



time_recursive_rounded = round(time_recursive, 5)

print(f"Time taken by recursive Binary Search : {time_recursive_rounded} seconds")

print("--------------------------------------------------------")


####################################################################################################
##Linear Search

tar_linear = 675

def linear_search(arr, tar_linear):
    if tar_linear in arr:
        return arr.index(tar_linear)
    else:
        return -1


time_linear = timeit.timeit(lambda: linear_search(arr, tar_linear), number=10000)

ans_linear = linear_search(arr, tar_linear)

if ans_linear != -1:
    print(f"Target is found at index :  {ans_linear}")
else:
    print("Not found")

time_linear_rounded = round(time_linear, 5)

print(f"Time taken by Linear search :  {time_linear_rounded} seconds")

            
                    