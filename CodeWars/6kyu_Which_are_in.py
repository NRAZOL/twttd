"""Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which
are substrings of strings of a2."""

def in_array(array1, array2):
    arr = []
    for a2 in array2:
        for a1 in array1:
            if a1 in a2 and a1 not in arr:
                arr.append(a1)
    return sorted(arr)