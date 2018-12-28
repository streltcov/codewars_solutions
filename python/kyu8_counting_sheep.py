# Consider an array of sheep where some sheep may be missing from their place
# We need a function that counts the number of sheep present in the array (true means present)

def count_sheeps(arrayOfSheeps):
    count = 0
    for sheep in arrayOfSheeps:
        if sheep == True:
            count = count + 1
    return count
