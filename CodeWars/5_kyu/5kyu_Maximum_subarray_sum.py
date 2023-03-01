"""The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or
list of integers:"""


def max_sequence(arr):
    max_sum = 0
    partialSum = 0

    for i in arr:
        partialSum += i
        partialSum = max(partialSum, 0)
        max_sum = max(partialSum, max_sum)
    return max_sum