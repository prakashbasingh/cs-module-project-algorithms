'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # iterate through array
    for i in range(len(arr)):
    # if i = 0 then pop and append 0
        if arr[i] == 0:
            popped_zero = arr.pop(i)
            arr.append(popped_zero)
    # then return arr
    return arr
    
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")