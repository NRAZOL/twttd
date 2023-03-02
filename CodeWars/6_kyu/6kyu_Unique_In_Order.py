'''https://www.codewars.com/kata/54e6533c92449cc251001667'''


def unique_in_order(sequence):
    newList = []
    for item in sequence:
        if len(newList) < 1 or not item == newList[len(newList) - 1]:
            newList.append(item)
    return newList