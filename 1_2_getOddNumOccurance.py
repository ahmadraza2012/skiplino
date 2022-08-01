def getOddOccurrence(arr, arr_size):
     
    for i in range(0,arr_size):
        count = 0
        for j in range(0, arr_size):
            if arr[i] == arr[j]:
                count+=1
             
        if (count % 2 != 0):
            return arr[i]
         
    return -1
     
# Call function and run test cases.
arr = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(getOddOccurrence(arr, len(arr)))

arr1 = [1,1,2,-2,5,2,4,4,-1,-2,5]
print(getOddOccurrence(arr1, len(arr1)))

arr2 = [1,1,1,1,1,1,10,1,1,1,1]
print(getOddOccurrence(arr2, len(arr2)))