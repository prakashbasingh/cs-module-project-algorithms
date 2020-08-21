'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(arr, k):
    # Your code here
    # create an empty array for the window
    # return the list of max value from that window
    # need to keep moving window towards the right one step at a time
    max_value_list = []
    for first_index in range(len(arr) - (k-1)):
        window_array = arr[first_index:first_index + k]
        max_value = max(window_array)
        max_value_list.append(max_value)
    
    return max_value_list



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
