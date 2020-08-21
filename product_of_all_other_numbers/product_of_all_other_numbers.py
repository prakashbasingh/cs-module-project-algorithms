'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # first create an new empty array/list
    new_array = []
    # iterating through array need to multiply all index expect the current index
    for i in range(len(arr)):
        # need to keep track of product
        product = 1
        for excluded_idx in range(len(arr)):
        # if current index is not equal to excluded-idx
            if i != excluded_idx:
            #multiply values of all other index except the excluded index
                product *= arr[excluded_idx] # or product = product * arr[i]
    # need to append product in the new array
        new_array.append(product)
    # then return the  new array with products of all numbers except the current index number
    return new_array

# O(n^2)
# def product_of_all_other_numbers(arr, excluded_idx=0, new_array=[]):
#     # base case(s)?
#     # when the excluded index (ex_i) is greater
#     # or equal to length of the arr
#     if excluded_idx >= len(arr):
#         return new_array
    
#     # otherwise
#     product = 1

#     # iterate through the arr
#     for i in range(len(arr)):
#         # if current i is not the excluded_idx
#         if i != excluded_idx:
#             # multiply value with product
#             product *= arr[i]
#     # append product to new_array
#     new_array.append(product)
#     # return a call to self with (arr, excluded_idx + 1, new_array)
#     return product_of_all_other_numbers(arr, excluded_idx + 1, new_array)

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
