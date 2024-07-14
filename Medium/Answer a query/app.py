# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and 
# an integer limit, return a boolean array that represents the answer to each query. 
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

# For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, 
# the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

def answer(nums, queries, limit):
    prefix=[0]*len(nums)
    for i in range(len(nums)):
        prefix[i]=nums[i]+prefix[i-1]

    res=[False]*len(queries)
    for i in range(len(queries)):
        if prefix[queries[i][1]] - prefix[queries[i][0]] + nums[queries[i][0]] <limit:
            res[i]=True
    return res

print(answer([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))