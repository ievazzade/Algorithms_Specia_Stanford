def mergeSort(nums):
    if len(nums)==1:
        return nums
    
    n = len(nums)

    left, right = mergeSort(nums[:n//2]), mergeSort(nums[n//2:])

    out = []
    i, j = 0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            out.append(left[i])
            i+=1
        else:
            out.append(right[j])
            j+=1
    if i<len(left):
        out += left[i:]
    if j<len(right):
        out += right[j:]
        
    return out
def msort(array):
    """
    Implement merge sort
    :param array: an unsorted list of integers
    :return: a sorted list of integers
    """
    if len(array) == 1:
        return array

    n = len(array)
    a, b = msort(array[:n // 2]), msort(array[n // 2:])
    return a, b

def main():
    print(mergeSort([1,6,5,4,3,7,8,9,2]))

if __name__ == '__main__':
    main()   
