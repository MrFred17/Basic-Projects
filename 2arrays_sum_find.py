# array1 = [7, 4, 1, 10]
# array2 = [4, 5, 8, 7]
# target: 13
# it is given that both arrays are the same length


def find_target_pair(arr1, arr2, target):  # Time: O(n log n)
    closest = float("-inf")
    pair = 0, 0
    array1 = sorted(arr1)
    array2 = sorted(arr2)

    a1_iterator = 0
    a2_iterator = -1

    looping = True
    while looping:
        try:
            a2  = array2[a2_iterator]
            a1 = array1[a1_iterator]
        except IndexError:
            break
        if a1 + a2 == target:  # Equal to target
            return a1, a2
        if ( abs(a2+a1) - target ) < ( abs(closest) ) and a2+a1 < target:  # Closer to target but smaller
            closest = a2+a1
            pair = a1, a2
            a1_iterator += 1
            if (a2_iterator == array2[0]) and (a1_iterator == array1[-1]):
                looping = False
        elif ( abs(a2+a1) - target ) < ( abs(closest) ) and a2+a1 > target:  # Closer to target but larger
            closest = a2+a1
            pair = a1, a2
            a2_iterator -= 1
            if (a2_iterator == array2[0]) and (a1_iterator == array1[-1]):
                looping = False
        elif (a2+a1) < target:   # For these negative numbers...
            a1_iterator += 1
        elif (a2+a1) > target:   # Again... negatives don't have the same calculation
            a2_iterator -= 1
    return pair


array1 = [5, -4, 3, 12, 20]
array2 = [9, 1, 11, 8, -7]

# Let's try with a sum of 20:
print(find_target_pair(array1, array2, 20))
# Yay! Worked. Returned 12 and 8!

# Now let's try a sum that is larger than all possible sums.
# The largest sum possible is 31. Let's see
print(find_target_pair(array1, array2, 36))
# Worked again! Returned 20 and 9!

# And now, the final challenge awaits!
# Let's test a negative result! (-2, for example)
print(find_target_pair(array1, array2, -2))
# Wo-Hoo! Worked, even for those filthy negatives




