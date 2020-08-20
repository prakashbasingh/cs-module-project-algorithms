'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # find the single number in the array/list
    # needing a data structure to keep track how many times a number appears
    # need to add value using loops
    # need to find the number which appears only once
    number = set()
    for x in arr:
        if x in number:
            number.remove(x)
        else:
            number.add(x)
    return number.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")